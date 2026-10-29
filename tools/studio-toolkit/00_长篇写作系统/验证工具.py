"""Small repeatable local checks; fixtures are not novel manuscripts."""
from pathlib import Path
import os
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get('FICTION_WORKSPACE', HERE.parent)).expanduser()
SKILLS = Path(os.environ.get('FICTION_SKILLS_DIR', ROOT / '.agents' / 'skills')).expanduser()
NAMES = ['story', 'story-setup', 'story-long-write', 'story-long-scan',
         'story-long-analyze', 'story-review', 'story-deslop']

def run(args):
    result = subprocess.run([str(x) for x in args], capture_output=True, text=True)
    return {'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}

def main():
    checks = []
    def record(name, passed, evidence):
        checks.append({'name': name, 'passed': bool(passed), 'evidence': evidence})

    record('seven_skill_entrypoints', all((SKILLS / n / 'SKILL.md').is_file() for n in NAMES), NAMES)
    needed = ['workflow-setup.md', 'workflow-chapter.md', 'long-format.md',
              'writing-craft.md', 'long-chapter-quality.md', 'long-chapter-hooks.md',
              'tracking-transaction.md']
    missing = [n for n in needed if not (SKILLS / 'story-long-write' / 'references' / n).is_file()]
    record('long_write_reference_dependencies', not missing, {'missing': missing})
    node = shutil.which('node')
    if not node:
        record('node_available', False, 'node not found')
    with tempfile.TemporaryDirectory(prefix='novel-skill-check-') as temp:
        root = Path(temp)
        bad = root / 'bad.txt'
        clean = root / 'clean.txt'
        bad.write_text('她失去的不是一封信，而是整个青春。\n命运的齿轮开始转动。\n', encoding='utf-8')
        clean.write_text('她把信封翻过来，封口还粘着半根线。\n“你拆过？”\n他伸出的手停在桌边，没有碰那封信。\n', encoding='utf-8')
        scanner = SKILLS / 'story-deslop' / 'scripts' / 'check-ai-patterns.js'
        if node:
            before = hashlib.sha256(bad.read_bytes()).hexdigest()
            result = run([node, scanner, '--check', '--json', '--fail-on=blocking', bad])
            findings = json.loads(result['stdout']).get('findings', []) if result['stdout'] else []
            types = {f['type'] for f in findings}
            record('style_known_patterns_detected', result['exit_code'] == 1 and
                   {'not-is-comparison', 'trailer-summary'}.issubset(types), result)
            record('style_scan_is_read_only', before == hashlib.sha256(bad.read_bytes()).hexdigest(), before)
            result = run([node, scanner, '--check', '--json', '--fail-on=blocking', clean])
            record('style_plain_control_not_blocked', result['exit_code'] == 0, result)

        project = root / 'state-fixture'
        project.mkdir()
        init = root / 'init.json'
        init.write_text(json.dumps({
            'schema_version': 1, 'book_title': '工具验收夹具', 'last_chapter': 0,
            'context': {'position': {'volume': '验收卷', 'volume_start_chapter': 1,
                                    'story_time': '开篇前', 'scene': '测试场景'},
                        'long_term_constraints': ['测试事实，不得用于小说'],
                        'active_character_names': [], 'continuity_risks': [],
                        'recent_chapters': [], 'next_chapter_commitments': ['待测试']},
            'character_snapshots': {}, 'foreshadow': [], 'timeline_events': []
        }, ensure_ascii=False), encoding='utf-8')
        tracker = SKILLS / 'story-long-write' / 'scripts' / 'tracking_commit.py'
        result = run([sys.executable, tracker, 'init', '--project', project, '--input', init])
        record('tracking_init', result['exit_code'] == 0, result)
        if result['exit_code'] == 0:
            result = run([sys.executable, tracker, 'check', '--project', project])
            record('tracking_initial_consistency', result['exit_code'] == 0, result)
            state = project / '追踪' / '_tracking-state.json'
            before = hashlib.sha256(state.read_bytes()).hexdigest()
            result = run([sys.executable, tracker, 'init', '--project', project, '--input', init])
            record('tracking_refuses_reinitialization', result['exit_code'] != 0 and
                   hashlib.sha256(state.read_bytes()).hexdigest() == before, result)
            context = project / '追踪' / '上下文.md'
            original = context.read_bytes()
            record('context_seven_sections_and_size',
                   sum(x.startswith('## ') for x in original.decode().splitlines()) == 7
                   and len(original) <= 12288, {'bytes': len(original)})
            context.write_text(original.decode() + '\n测试：此处被故意误改。\n', encoding='utf-8')
            result = run([sys.executable, tracker, 'check', '--project', project])
            record('tracking_detects_corrupted_view', result['exit_code'] != 0 and
                   'derived view differs' in result['stderr'], result)
            context.write_bytes(original)  # restore only our synthetic fixture
            result = run([sys.executable, tracker, 'check', '--project', project])
            record('fixture_restoration_checks', result['exit_code'] == 0, result)

    report = {'tested_at_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'Tool smoke checks only; no manuscript quality or independent-agent claim.',
              'checks': checks, 'passed': all(x['passed'] for x in checks)}
    Path(os.environ.get('FICTION_CHECK_REPORT', HERE / '工具验收结果.json')).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'passed': report['passed'], 'checks': len(checks),
                      'failed': [x['name'] for x in checks if not x['passed']]}, ensure_ascii=False))
    return 0 if report['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
