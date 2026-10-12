#!/usr/bin/env python3
"""List continuity-sensitive wording for human review, never classify it as an error.
Usage: python flag_continuity_claims.py draft.txt [...] [--output report.json]
No manuscript or index modifications. It cannot establish semantic consistency.
"""
import argparse, hashlib, json, re
from pathlib import Path
PATTERNS = {
    'absolute_or_first': r'第一次|从未|从来没有|从来不|一直都是|唯一',
    'past_scene_recall': r'想起|记得|上一次|第一次来',
    'calendar_anchor': r'(?:[一二三四五六七八九十]+|\d+)月(?:[一二三四五六七八九十]+|\d+)[日号]|国庆|中秋',
}
def inspect(path):
    p=Path(path);raw=p.read_bytes();text=raw.decode('utf-8');items=[]
    for number,line in enumerate(text.splitlines(),1):
        if not line.strip(): continue
        for category,pattern in PATTERNS.items():
            matches=[m.group() for m in re.finditer(pattern,line)]
            if matches: items.append({'line':number,'category':category,'triggers':matches,'context':line})
    return {'source_path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'flags':items}
def main():
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('paths',nargs='+');a.add_argument('--output');args=a.parse_args()
    report={'status':'review_triggers_not_error_verdicts','limits':'回读原场景及同义动作；绝对词可以正确。新增日历锚点须回归相关旧章和当年节假日。旗标数量不是错误数或质量评分。','documents':[inspect(x) for x in args.paths]}
    out=json.dumps(report,ensure_ascii=False,indent=2)+'\n'
    if args.output: Path(args.output).write_text(out,encoding='utf-8')
    else: print(out,end='')
if __name__=='__main__': main()
