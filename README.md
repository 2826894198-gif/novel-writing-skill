# 长篇创作工作室辅助工具

**把创作里的重复检查交给工具，让文本问题、状态偏差和运营数据有迹可查。**

从小说工作室中抽取的 Python 辅助脚本，用于外部写作技能的隔离冒烟检查、文本风险词初筛和平台 CSV 的本地规则评估。

> 当前阶段：集成脚本归档；独立运行需要适配路径并配置外部技能和输入目录。本仓库为 2026-10-28 整理的源码快照，原项目继续保留在本地。

## 项目亮点

- 验证外部 story 系列技能入口与必要参考依赖是否齐全
- 用合成文本检查风格扫描的预期触发与只读性
- 在临时目录验证追踪初始化、一致性、重复初始化拒绝和派生视图损坏检测
- 对 Markdown 中的仿写、参考具体作品等风险措辞做词表初筛
- 将平台 CSV 中的阅读、收藏、更新和反馈字段按显式规则转为本地评估记录

## 技术实现

Python 3 标准库 · Node.js 外部扫描器 · CSV · JSON · Markdown · 外部 oh-story-claudecode skills

- 00_长篇写作系统/验证工具.py
- 90_自动化脚本/originality_check.py
- 90_自动化脚本/auto_evaluate.py

## 快速开始

Python 辅助脚本使用环境变量定位工作区，默认指向仓库内的 `projects/` 与 `data/private/`。先用随库合成目录演练：

```bash
FICTION_PROJECTS_DIR=examples/projects python3 90_自动化脚本/originality_check.py
FICTION_DATA_INBOX=examples FICTION_PROJECTS_DIR=examples/projects python3 90_自动化脚本/auto_evaluate.py
```

第二条命令会在虚拟项目中生成 `数据评估.md`（已忽略），不会连接平台。输入 CSV 为从零编造的空运营夹具。真实作品与平台 CSV 仅放本地私有目录，配置项见 `.env.example`；示例文件需通过 shell 导出，脚本不会自动加载 dotenv。

完整技能冒烟检查依赖另外安装的 oh-story 技能与 Node.js。配置实际技能目录后运行：

```bash
FICTION_SKILLS_DIR=/path/to/story-skills python3 00_长篇写作系统/验证工具.py
```

缺少外部技能时该检查不能通过。这里只保留集成层与上游许可说明，不把上游全部工具或 MIT 授权扩展为本仓库所有内容的授权。

## 目录导航

```text
00_长篇写作系统/
90_自动化脚本/
docs/
```

## 交付状态与证据

- 00_长篇写作系统/验证工具.py
- 00_长篇写作系统/UPSTREAM-LICENSE.txt
- 90_自动化脚本/README.md
- 90_自动化脚本/originality_check.py
- 90_自动化脚本/auto_evaluate.py

- 不包含小说正文、真实作品资料、后台记录、个人自动任务状态或实际运营数据
- 暂存版已将本机绝对路径改为环境变量；完整技能检查仍需配置外部依赖
- 工具验证只覆盖机械行为；无告警不等于语义正确，也不代表已部署独立专家审稿或多 Agent 系统
- 风险词扫描不能判断抄袭或替代法律判断；规则评分不代表真人阅读质量或商业收益
- auto_evaluate.py 的后台抓取是预留方向，当前读取本地 CSV；不自动发布
- 源码中包含具体作品示例的工作簿生成脚本、执行约定及私有验收输出不进入通用工具包
- 历史验收结果仅作来源侧线索，本轮未重新运行外部技能与工具检查

本次整理的核验结果见 [仓库状态](docs/REPOSITORY_STATUS.md)，项目介绍口径见 [展示说明](docs/SHOWCASE.md)。

## 协作与使用

- 安装依赖前核对项目所需运行时，配置文件使用示例值；凭据和真实业务数据不进入 Git。
- 提交与反馈请见 [CONTRIBUTING.md](CONTRIBUTING.md)；敏感问题处理见 [SECURITY.md](SECURITY.md)。
- 许可证与第三方资源见 [RIGHTS.md](RIGHTS.md)。公开访问不等于获得所有素材的再分发许可。
