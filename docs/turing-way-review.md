# The Turing Way 与参考论文对本 skill 的审视

本次按主题核对原文与现行 skill，未声称全文阅读全部手册或历史参考论文。结论：现有来源、结果分层和执行工具值得保留；应加强接手、协作和证据声明，并限制无效记录负担。

## 来源与推导

| 来源及本次范围 | 原文支持的方向 | 本 skill 的设计推导 |
|---|---|---|
| The Turing Way：guiding-principles，本地正文 | 包容、透明、赋能；开放与必要限制并存 | PROJECT 增加参与和访问说明，避免层层重复审批 |
| The Turing Way：Collaborative project documentation，本地正文 | 新人导向说明、角色、贡献、许可、计划与过程 | 增加接手复跑模板、实际贡献与求助入口 |
| The Turing Way：Definitions，本地正文 | 复现、复核、稳健与推广区分；受限数据仍可讨论复现 | findings 分开记录证据维度 |
| Stoudt、Vásquez、Martinez（2021），官方摘要与工作流定义；本地旧稿对照 | Explore／Refine／Produce，可往返；研究工作流不同于计算 pipeline | 保留目录，按阶段调节完善程度，不把 Snakemake 成功当研究完成 |
| Wilson 等（2017），官方摘要与结论 | 可实践、可逐步采用的科研计算习惯 | 优先最小有效记录、现有工具和明确交接，不追求文档数量 |
| Ziemann 等，五支柱，本地端到端自动化和环境相关段落 | 减少手工步骤，保留不可避免的清理过程；降低复跑成本 | 增加环境恢复、手工步骤和预期输出检查 |

以上目录、字段和触发规则是本套设计，不冒充来源直接要求。两份 AI／架构资料继续用于对象、接口和 ADR；不以软件工程完整度替代科研判断。

## 具体改进

1. 阶段要求：Explore 记录必要证据，Refine 加强可比性与复用，Produce 面向接手与固定成果。
2. 质量声明：计算复现、稳健性、新数据复核、推广范围分别核对。
3. 协作：受众、角色、贡献、求助和审阅方式进入 PROJECT，不另建平行系统。
4. 可访问：材料分开记录访问和许可；合成样例明确用途边界。
5. 复跑：固定目标、恢复环境、实际命令、预期结果与容差、偏差和日期。
6. 可持续：维护责任、最后验证、退出和取回方式进入 release。

## 原文入口与版本提醒

- [The Turing Way](https://book.the-turing-way.org/)。guiding-principles、pd-overview-repro、overview-definitions 位于 [book/website](https://github.com/book/the-turing-way/tree/main/book/website)；使用本次读取的版本，不声称与网站最新文本逐字一致。
- [Stoudt 等正式发表版本](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008770)。正式年份为 2021，阶段为 Explore／Refine／Produce。旧本地稿的 Exploratory／Refinement／Polishing 不作为当前规范术语。
- [Wilson 等（2017）](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)。
- Ziemann 等正式发表版本：<https://doi.org/10.1093/bib/bbad375>；仅将核对段落用作机制依据，不据文件名追加未经核对的发表信息。

## 不扩大承诺

没有改变用户确定的目录，没有新增平台，没有强制每个探索运行都做完整发布。模板新增字段尚未成为自动闸门，实际项目也未因此取得独立复现或外部验证证据。
