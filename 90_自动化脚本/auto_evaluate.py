#!/usr/bin/env python3
"""
AI 小说工作室自动评估脚本。

当前版本做三件事：
1. 读取 06_评估系统/data_inbox/平台数据.csv 或 平台数据模板.csv。
2. 按评分规则生成初步评估。
3. 将结果写入每个项目的 数据评估.md。

后续如需接入平台后台抓取，可在 fetch_platform_data() 中增加
“用户已登录浏览器页面读取”的逻辑。不要保存账号密码。
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
import os
from pathlib import Path


ROOT = Path(os.environ.get("FICTION_WORKSPACE", Path(__file__).resolve().parents[1])).expanduser()
INBOX = Path(os.environ.get("FICTION_DATA_INBOX", ROOT / "data" / "private")).expanduser()
CSV_PATH = INBOX / "平台数据.csv"
TEMPLATE_CSV_PATH = INBOX / "平台数据模板.csv"
PROJECTS_DIR = Path(os.environ.get("FICTION_PROJECTS_DIR", ROOT / "projects")).expanduser()


@dataclass
class PlatformRow:
    date: str
    project: str
    platform: str
    words: int
    daily_words: int
    exposure: int
    reads: int
    saves: int
    follows: int
    comments: int
    daily_income: float
    total_income: float
    signed: str
    recommended: str
    feedback: str


def to_int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def to_float(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def read_rows() -> list[PlatformRow]:
    source = CSV_PATH if CSV_PATH.exists() else TEMPLATE_CSV_PATH
    rows: list[PlatformRow] = []
    with source.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for item in reader:
            rows.append(
                PlatformRow(
                    date=item.get("日期", ""),
                    project=item.get("项目", ""),
                    platform=item.get("平台", ""),
                    words=to_int(item.get("当前字数", "")),
                    daily_words=to_int(item.get("当日更新", "")),
                    exposure=to_int(item.get("曝光", "")),
                    reads=to_int(item.get("阅读", "")),
                    saves=to_int(item.get("收藏书架", "")),
                    follows=to_int(item.get("追更", "")),
                    comments=to_int(item.get("评论", "")),
                    daily_income=to_float(item.get("当日收益", "")),
                    total_income=to_float(item.get("累计收益", "")),
                    signed=item.get("是否签约", ""),
                    recommended=item.get("是否推荐", ""),
                    feedback=item.get("读者主要反馈", ""),
                )
            )
    return rows


def score_row(row: PlatformRow) -> tuple[int, str, list[str]]:
    if row.words == 0 and row.reads == 0 and row.total_income == 0:
        return 0, "方案期/待开发", ["尚未发布，不进入止损判断；优先完成书名、简介、大纲和前三章。"]

    platform_score = 0
    if row.signed == "是":
        platform_score += 12
    if row.recommended == "是":
        platform_score += 8

    read_score = min(20, row.reads // 100)
    if row.exposure and row.reads:
        click_rate = row.reads / max(row.exposure, 1)
        if click_rate >= 0.1:
            read_score = max(read_score, 15)
        elif click_rate >= 0.05:
            read_score = max(read_score, 10)

    retention_score = min(20, row.saves // 20 + row.follows // 10 + row.comments)
    content_score = 10
    if row.words >= 20000:
        content_score += 4
    if row.daily_words >= 4000:
        content_score += 3
    if "AI" in row.feedback or "流水账" in row.feedback or "太慢" in row.feedback:
        content_score -= 4
    content_score = max(0, min(20, content_score))

    income_score = min(10, int(row.total_income // 50))
    risk_penalty = 0
    if "违规" in row.feedback or "抄袭" in row.feedback or "审核" in row.feedback:
        risk_penalty += 5
    if row.words >= 30000 and row.signed != "是" and row.reads < 1000:
        risk_penalty += 4

    total = platform_score + read_score + retention_score + content_score + income_score - risk_penalty
    total = max(0, min(100, total))

    if total >= 80:
        verdict = "强继续"
    elif total >= 65:
        verdict = "继续优化"
    elif total >= 50:
        verdict = "观察整改"
    elif total >= 35:
        verdict = "高风险"
    else:
        verdict = "止损/暂不投入"

    actions: list[str] = []
    if row.exposure and row.reads / max(row.exposure, 1) < 0.05:
        actions.append("点击偏低，优先优化书名、简介和标签。")
    if row.reads and row.saves / max(row.reads, 1) < 0.03:
        actions.append("收藏偏低，检查前三章承诺是否足够强。")
    if "太慢" in row.feedback:
        actions.append("读者反馈节奏慢，压缩铺垫，增加每章事件推进。")
    if "AI" in row.feedback or "流水账" in row.feedback:
        actions.append("疑似 AI 味反馈，重写关键段落，增加具体动作和人物语气。")
    if not actions:
        actions.append("保持观察，等待更多数据。")

    return total, verdict, actions


def find_project_dir(project: str) -> Path | None:
    for path in PROJECTS_DIR.iterdir():
        if path.is_dir() and path.name == project:
            return path
    return None


def append_project_report(row: PlatformRow, score: int, verdict: str, actions: list[str]) -> None:
    project_dir = find_project_dir(row.project)
    if not project_dir:
        return
    report_path = project_dir / "数据评估.md"
    record_date = row.date or date.today().isoformat()
    marker = f"## 自动评估记录：{record_date}"
    if report_path.exists() and marker in report_path.read_text(encoding="utf-8"):
        return
    action_lines = "\n".join(f"- {action}" for action in actions)
    block = f"""

{marker}

| 项目 | 内容 |
|---|---|
| 平台 | {row.platform} |
| 当前字数 | {row.words} |
| 当日更新 | {row.daily_words} |
| 曝光 | {row.exposure} |
| 阅读 | {row.reads} |
| 收藏/书架 | {row.saves} |
| 追更 | {row.follows} |
| 评论 | {row.comments} |
| 当日收益 | {row.daily_income} |
| 累计收益 | {row.total_income} |
| 是否签约 | {row.signed} |
| 是否推荐 | {row.recommended} |
| 读者反馈 | {row.feedback} |
| 自动评分 | {score} |
| 自动结论 | {verdict} |

### 建议动作

{action_lines}
"""
    with report_path.open("a", encoding="utf-8") as f:
        f.write(block)


def main() -> None:
    rows = read_rows()
    for row in rows:
        score, verdict, actions = score_row(row)
        append_project_report(row, score, verdict, actions)
        print(f"{row.project}: {score} - {verdict}")


if __name__ == "__main__":
    main()
