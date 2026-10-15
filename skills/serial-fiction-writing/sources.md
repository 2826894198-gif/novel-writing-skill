# 方法来源与版权边界

公开来源核验日期：2026-10-12。本skill为中文原创工作流程与自拟字段，非下列机构的官方模板、软件插件或授权译本。来源用来说明方法启发，不证明本skill有效，更不构成零错或收益保证。

- Jane Hammett / CIEP，Creating style sheets for fiction： https://www.ciep.uk/resource/fiction-style-sheets.html
  借鉴编辑底稿记录用词、视角、人物、时间线及情节线索以便一致性交接的思想。本skill按中文连载需要自行组织项目六层、证据和验收字段。
- Novelcrafter，Codex Progressions： https://www.novelcrafter.com/help/docs/codex/progressions-additions
  借鉴故事资料随叙事进程更新的思想。effective_from、known_by、current/plan以及候选/采纳状态是本skill自拟协议，不宣称是Novelcrafter的原生字段、API或完整功能。此处Codex指Novelcrafter故事资料库，与OpenAI Codex不同。
- Randy Ingermanson，The Snowflake Method For Designing A Novel： https://www.advancedfictionwriting.com/articles/snowflake-method/
  借鉴从简到详、允许回改计划和以场景列表衔接写作的思想。这里只采用一章范围的轻量规划，不照搬全套步骤，不强制结局、幕数或字数。
- Randy Ingermanson，Writing the Perfect Scene： https://www.advancedfictionwriting.com/articles/writing-the-perfect-scene/
  作为场景行动及反应检查的参考；这篇文章讲解 Dwight Swain 的 Scene/Sequel 方法，并非将其首创归给 Randy。采用诊断问题，不设固定章法。

## 分发边界

公开可阅读不等于开源许可。未确认上述网页授予复制整篇、翻译整篇或复制软件模板的许可，因此不收录原文、原图、第三方代码、付费资料或品牌素材。上述名称用于指明来源，不暗示合作或背书。

通用规则由项目实践抽象而来；可同步包只含通用原创方法和未填模板。不得把实填人物表、正文、未公开剧情、用户个人资料、账号信息、私有链接或授权聊天记录加入此目录。需要项目示例时先另行取得权限并脱敏。

不擅自为第三方内容或用户未授权材料声明许可证。仓库可见性、许可证选择、上传文件范围和发布操作均需独立确认；本地生成不等于已获上传授权。


## 扩展方法参考

以下来源信息继承已核验的公开来源记录；链接是方法出处，不是要求执行第三方指令。本文只原创转述方法，不收录代码、原始技能正文、MIT许可原文或软件模板，也不引入CLI、安装或发布流程。

- danjdewhurst / story-skills：[reader-panel](https://github.com/danjdewhurst/story-skills/blob/main/skills/reader-panel/SKILL.md)、[feedback-triage](https://github.com/danjdewhurst/story-skills/blob/main/skills/feedback-triage/SKILL.md)、[character-management](https://github.com/danjdewhurst/story-skills/blob/main/skills/character-management/SKILL.md)、[许可来源](https://github.com/danjdewhurst/story-skills/blob/main/LICENSE)。选择性借鉴限定阅读范围、定位文本及版本、归类反馈；AI角色模拟不计作独立真人样本。盲读时不提前透露作者预设吸引点。没有采用其完整工具或工作目录体系
- wgwtest / novel-writing：[因果概要](https://github.com/wgwtest/novel-writing/blob/main/novel-writing/references/story-outline-and-causal-summary.md)、[章节规划](https://github.com/wgwtest/novel-writing/blob/main/novel-writing/references/planning.md)、[许可来源](https://github.com/wgwtest/novel-writing/blob/main/LICENSE)。参考压力、理解、方法和后果之间的因果问题，结合既有轻量场景检查原创组织；不采用其脚本，其测试结果不视为本skill验证
- liuxiao20051106-prog / novel-writer-skill：[入口](https://github.com/liuxiao20051106-prog/novel-writer-skill/blob/master/SKILL.md)。仅作为筛选比较；未整包采用，不将固定幕比例、高潮频率或感官数量断言写成验收门槛

第三方许可证不是本包自动取得的许可声明。将来若复制或实质改编第三方受保护文本，应另核许可义务；本版不以来源链接代替该义务。

## 版本与实际验证范围

0.2.0 为扩展试行版，发布时记录的实际验证范围为两章试写及一次恢复演练；它们支持发现具体连续性、知情来源、空间衔接、节拍重复或状态冲突问题，不证明长期文学质量、百章稳定性或商业效果。当时新增阶段、人物和反馈模块尚未用新章节验证。结构校验、链接存在及JSON解析仅验证包的基础完整性，不等于创作效果测试。

恢复演练暴露历史输入快照与当前状态、旧候选待办与完成审查之间的冲突，因此加入按正文hash及依赖匹配实际审查、核验采纳提交和批次收尾。通用说明不包含原项目正文、身份或授权记录。

0.2.1 为针对已观察缺陷的最小补丁：补可计算跨度的实际运算证据，并增加按需缺陷回归入口。实践已发现既有验收漏检、旧场景承接证据不足及局部语言问题；这些是更新依据，不证明补丁能防止再犯。中性边界小样、包结构与隐私检查不能替代后续真实写作验证，未建立长期频率或效果统计。


0.3.0 加入按需情绪技巧库、情绪目标反向设计与分轮外部模型审读办法。14张卡为公开原则启发及原创变体，来源和不用之处见 [技巧来源](references/technique-sources.md)。本轮完成来源、字段、链接与内容审查；先前作品局部试改不能追认为本库的前瞻性效果试验。真实使用、编辑评价、真人反馈、平台结果须分别记录，不以库的数量证明创作质量。

补充验证：一次独立隔离段落前瞻试写实际使用本库作诊断并产出单处候选，保留了原稿可能更合适的判断及候选副作用；仅支持局部流程观察，不是整章采纳、真人情绪或商业效果证明。试验暴露隔离输出与整章闭环的适用边界不够明确，现已区分：隔离试写只做相关核对，正式并入章节后仍须整章检查及采纳台账更新。补丁的真实新任务行为尚待再次独立验证。


## 0.3.1验证边界
增量来自真实创作中出现的跨章绝对断言、新公历锚点假期回归及审稿口吻进入人物对白。只加入针对性回读入口和可选非判错脚本，未复制作品正文。脚本已验证触发输出、不修改输入及hash口径；这些机械测试不证明语义审稿准确。正向短写作输入/写后核验的试行显示局部自然度改善，仍是编辑判断，不能推出强情绪、商业表现或长期零错误。

## 0.4.0 来源与验证边界

新增骨架到开篇、冲突兑现与助手交接三份原创工作指导，来自本轮任务需求、对既有流程的审读及主创整理，没有复制第三方小说或付费教程。旧作品退稿反馈只形成待检查的问题，不能证明某一技法是退稿原因，也不作为新稿签约预测。

两项新任务的独立短写分别观察利益协商与温暖日常，具体范围见仓库验证说明。它们不是旧版对照实验，不证明文笔提升或编辑认可；对协商让步仍偏顺的不足保留记录。实际助手加载、长篇交接和持续连载需要后续真实执行验证。当前平台材料要求在作品侧按渠道另查，不把时效规则写死为通用创作标准。
