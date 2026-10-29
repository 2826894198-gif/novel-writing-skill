# 创作辅助脚本

本目录只保留与具体作品分离的集成脚本。

- `originality_check.py`：对配置目录中的 Markdown 做风险词初筛，不改正文，不裁定侵权。
- `auto_evaluate.py`：读取本地 CSV 并向对应项目追加规则评估；不连接后台、不自动发布。

输入目录通过 `FICTION_PROJECTS_DIR`、`FICTION_DATA_INBOX` 与 `FICTION_WORKSPACE` 配置，合成演示命令见仓库根目录 README。真实作品、运营数据、账号凭据与自动任务状态不进入 Git。评分规则只是辅助判断，不证明阅读效果或收益。
