# research-project 阅读导航

当前形态：一个总 skill，内部七个动作模块与六个结构模块。先从 [总入口](../SKILL.md) 选择动作和涉及结构，实例化时同时填写项目自己的架构与样例。

## 公开版说明

本公开版使用合成名称与合成路径：项目名、研究代号、计划名、配置与脚本名、绝对路径和运行标识都已替换为 `示例项目`、`<project-root>` 一类占位符；示例中的数值、run 标识与文件计数均为示意值，不对应任何真实研究。

本地归档、原文快照、来源清单和会话记录不在本包内。文中出现的 `<reference-archive>`、`<paper-library>` 等占位符只表示“本地有、本包不含”，不能当作可取回证据。

现行规则看两处：结构层在 [structures/](../structures/project/GUIDE.md)（目录职责、文件归属、记录格式），动作层在 [modules/](../modules/organize/GUIDE.md)（各动作的流程与样例）。历史设计书和深读记录只作沿革与依据，不覆盖这两层正文。

| 阅读目标 | 正文与样例 |
|---|---|
| 两层怎样组合 | [整体架构](system-architecture.md)、[本次依据与取舍](two-layer-design.md) |
| 完整项目长什么样 | [整体结构](../structures/project/GUIDE.md)、[完整实例](../structures/project/EXAMPLE.md) |
| 文档、计划和任务 | [文档结构](../structures/documents/GUIDE.md)、[实例](../structures/documents/EXAMPLE.md) |
| 每份 PLAN 怎样集中说明数据、代码、结果和参考资料 | [计划资源规则](../structures/documents/GUIDE.md#本计划资源与目录)、[填写样例](../structures/documents/EXAMPLE.md#本计划资源与目录示例)、[两个编码助手案例依据](plan-resources-review.md) |
| 代码、配置及内部模块 | [代码结构](../structures/code/GUIDE.md)、[实例](../structures/code/EXAMPLE.md) |
| 单模态／多模态数据 | [数据结构](../structures/data/GUIDE.md)、[实例](../structures/data/EXAMPLE.md) |
| 结果根、run 与数据入口 | [结果结构](../structures/results/GUIDE.md)、[实例](../structures/results/EXAMPLE.md) |
| 采用记录和交付包 | [交付结构](../structures/delivery/GUIDE.md)、[实例](../structures/delivery/EXAMPLE.md) |
| 创建、整理、迁移 | [动作](../modules/organize/GUIDE.md)、[操作实例](../modules/organize/EXAMPLE.md) |
| 生成模板与校验 | [模板指南](template-guide.md) |
| 执行、判读和模块交接 | [执行流程](snakemake-workflow.md)、[结果工作流](results-workflow.md)、[协作契约](architecture-contract.md) |
| 文件归属、归档、临时区 | [归属规则](../structures/project/placement-rules.md) |
| 与 Superpowers 共用计划 | [协作约定](skill-interoperability.md) |

以下保留背景索引；历史设计书用于溯源，不替代上述现行正文。

> 当前安装形态：一个 research-project skill，含七个动作模块与六个结构模块。历史“五／六个内部模块”描述仅说明沿革；入口以根 SKILL.md 为准。

# Research skill 文档索引

日常使用先读短规范，设计和证据按需展开；不把全套资料塞进每次上下文。

| 需要回答的问题 | 文档 | 角色 |
|---|---|---|
| 大项目、小项目和代码／数据架构怎样统一？ | [项目架构规范](../structures/project/scope.md) | 层级、模块边界、依赖与渐进接入 |
| 每个具体项目最终怎么组织、谁更新记录？ | [具体项目结构规范](../structures/documents/GUIDE.md) | 当前确定的目录职责、必填记录、更新触发与周期检查 |
| 今天怎么开工、判断、收尾？ | [日常操作规范](daily-operations.md) | skill 内日常规则的唯一维护正文 |
| 早期设计怎样形成、工具怎样接入？ | [设计书](design-plan.md) | 架构、模板、实施顺序与验收规划 |
| 为什么采用这些原则和工具？ | [深读与工具证据](deep-reading-evidence.md) | 阅读范围、论文观点、工具源码观察及后续纠正 |
| 某条机制从哪里来？ | [机制溯源](mechanism-provenance.md) | 原则与历史出处的对应及待复核状态 |
| 早期完整规则是什么？ | [历史 v12](historical-v12.md) | 历史参考，不能覆盖当前决定 |
| 哪些已真正运行验证？ | [首版实施报告](implementation-report.md) | 实测范围与未完成项 |

## 当前决定与历史材料的边界

Snakemake 与 RO-Crate 已在本地首版接通；Aim 后置可选；Opik 不引入。六行判断条为默认简版，可由问题模板等价承载。安全、备份、终评和论文采用检查由 skill 执行，现有程序未自动强制全部检查。设计书的未来要求不当成已实现能力。

深读稿保留当时观察，页首注明已变化的决定；不是本次重新全文核验全部论文与软件。原始论文、书籍、工具源码和真实项目材料只引用，不复制。历史材料中的绝对路径与真实项目背景已替换为合成材料。

## 维护与来源

本目录是 skill 文档维护入口，原资料目录保留为来源，未经明确同步不双向覆盖。references/daily-operations.md 和 references/mechanism-provenance.md 只作兼容跳转，不再维护重复正文。

本包不保存原文快照、来源清单和链接审计结果；需要逐字节溯源时回到本地归档核对。编辑当前文档不改写历史材料；后续导入先比较源摘要和当前改动，再合并，不能直接覆盖。文档同时只允许一个写入者，写前重读、落盘前检查基线。

标注为缺失或本地归档的历史链接不能作为已经可取回的证据；链接检查不验证网页，也不证明内容正确。

## 计划管理专项

方向、多个 plan、任务依赖、排序和跨会话恢复由 [plan](../modules/plan/GUIDE.md) 专门管理。当前为一个 skill 总入口＋动作／结构两层模块；历史五件套描述保留为沿革。

## 当前协作架构

- [协作架构契约](architecture-contract.md)：两层模块的输入输出、责任、依赖、恢复与质量检查。
- [架构决策模板](../assets/templates/architecture-decision.md)：借鉴 MADR，记录取舍、落实核对与演进。
- [架构资料阅读与取舍](architecture-sources.md)：awesome-architecture 与 MADR 的采用范围。

## 当前文档层级（修订 4）

docs/PROJECT.md → docs/plans/{plan_id}/PLAN.md、TASK.md、LOG.md；其他材料按需创建。各层文件职责与结果／决定归属见 [结构规范](../structures/documents/GUIDE.md)。[PROJECT 模板](../assets/templates/project-contract.md)、[PLAN 模板](../modules/plan/assets/PLAN.md)、[TASK 模板](../modules/plan/assets/TASK.md) 配套使用。

本次对话要求的落点与实际验证见 [完整性核对](completeness-review.md)。

研究取舍与分阶段实施见 [研究原则](research-principles.md)；其来源与对现有 skill 的审视见 [The Turing Way 与论文](turing-way-review.md)。

新增项目与运行目录样板见 [模板指南](template-guide.md)；硬件和随机性记录兼容见 [v2 说明](record-v2.md)。

八项优化建议的落实与实测见 [v2 改进记录](improvement-v2-review.md)。
