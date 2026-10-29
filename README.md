# 中文长篇写作工作流

**让长篇写作有事实依据，修订有版本，换一个助手也能接着做。**

围绕长篇创作最容易失控的事实漂移、修订覆盖和跨助手接续，建立从故事骨架、逐章写作到审查采纳的工作流。通用方法与具体作品分开，创作风格由作品决定。辅助工具补充风险词初筛、外部技能检查和本地 CSV 规则评估。

> 当前阶段：写作 Skill 为 v0.4.0 扩展试行版，长期创作效果继续验证。2026-10-29 将 Skill 与辅助检查工具合为一个项目，原技能安装路径和各部分使用方式保留。

## 项目亮点

- 事实、人物误信和未来计划分别记录，审查时回到正文核对。
- 候选稿、差异、审查与采纳记录相互关联，保留恢复入口。
- 按任务加载技巧与资料，提供批次收尾和助手交接模板。

## 技术实现

SKILL.md · Markdown 工作流 · JSON 模板 · Python 辅助扫描

- skills/serial-fiction-writing/SKILL.md：主入口
- skills/serial-fiction-writing/assets/templates/：空白项目模板
- tests/validation-summary.md：实际验证记录

## 快速开始

先阅读技能入口，将完整目录交给支持 `SKILL.md` 的助手。在独立虚构样例项目中接入事实与当前稿件，再按入口逐章执行。

```bash
# 可选：查看连续性措辞初筛工具的用法
python3 skills/serial-fiction-writing/scripts/flag_continuity_claims.py --help
```

此脚本只定位候选措辞，不自动判断文学或事实错误。

## 目录导航

```text
docs/
skills/
tests/
tools/studio-toolkit/
```

## 交付状态与证据

- tests/validation-summary.md
- skills/serial-fiction-writing/sources.md

- 辅助脚本只定位候选措辞，事实判断、审稿与正式采纳由作者完成。
- 未验证长期文学效果、平台通过率或收益；仓库不含作品正文或私人人物资料。

本次整理的核验结果见 [仓库状态](docs/REPOSITORY_STATUS.md)，项目介绍口径见 [展示说明](docs/SHOWCASE.md)。

## 协作与使用

- 安装依赖前核对项目所需运行时，配置文件使用示例值；凭据和真实业务数据不进入 Git。
- 提交与反馈请见 [CONTRIBUTING.md](CONTRIBUTING.md)；敏感问题处理见 [SECURITY.md](SECURITY.md)。
- 许可证与第三方资源见 [RIGHTS.md](RIGHTS.md)。公开访问不等于获得所有素材的再分发许可。


历史实现说明保存在 [原项目说明](docs/ORIGINAL_README.md)，当前配置与状态以本页为准。

## 辅助检查工具

原 `fiction-studio-toolkit` 内容统一放在 [tools/studio-toolkit/](tools/studio-toolkit/README.md)。Python 标准库即可运行以下两个本地工具。从本仓库根进入工具目录后，用随库合成项目和 CSV 演练：

```sh
cd tools/studio-toolkit
FICTION_PROJECTS_DIR=examples/projects python3 90_自动化脚本/originality_check.py
FICTION_DATA_INBOX=examples FICTION_PROJECTS_DIR=examples/projects python3 90_自动化脚本/auto_evaluate.py
```

CSV 评估会在合成项目中生成忽略的 `数据评估.md`，只读取本地文件，不连接平台或自动发布。实际作品、平台记录和私人配置继续放在私有目录。

完整外部技能检查另外依赖自行安装的 **oh-story 技能与 Node.js**，在工具目录配置 `FICTION_SKILLS_DIR` 后运行 `00_长篇写作系统/验证工具.py`。缺少外部技能时该检查不能通过；第三方依赖不因为合并而成为本项目自主实现。

工具做机械初筛，由作者判断事实、文学质量和采纳结果。合并验证见 [docs/MERGE_VALIDATION.md](docs/MERGE_VALIDATION.md)，辅助工具原有权利说明和上游许可分别保留。
