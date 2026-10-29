#!/usr/bin/env python3
"""
基础原创性风险检查脚本。

注意：这个脚本不能法律意义上证明“不侵权”，只能做本地文本层面的
初筛，帮助发现明显风险词、仿写提示、可疑表达。

真正的侵权规避还需要人工判断：核心设定、人物关系、关键情节链、
书名简介是否与具体作品高度相似。
"""

from __future__ import annotations

import os
from pathlib import Path


ROOT = Path(os.environ.get("FICTION_WORKSPACE", Path(__file__).resolve().parents[1])).expanduser()
PROJECTS_DIR = Path(os.environ.get("FICTION_PROJECTS_DIR", ROOT / "projects")).expanduser()

RISK_TERMS = [
    "模仿",
    "仿写",
    "洗稿",
    "照着",
    "参考《",
    "像《",
    "某某作者风格",
    "续写《",
    "续写某",
    "改写成",
]


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    findings = []
    for term in RISK_TERMS:
        if term in text:
            findings.append(f"{path}: 命中风险词 `{term}`")
    return findings


def main() -> None:
    findings: list[str] = []
    for path in PROJECTS_DIR.rglob("*.md"):
        findings.extend(check_file(path))

    if findings:
        print("发现需要人工复核的原创性风险：")
        for item in findings:
            print("-", item)
    else:
        print("未发现明显仿写/洗稿提示词风险。仍需人工检查核心设定和情节链。")


if __name__ == "__main__":
    main()
