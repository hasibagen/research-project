---
name: research-project
description: 科研项目管理：按动作层处理创建整理、计划、代码、运行、判读与交付，按结构层约束整体项目、文档、代码配置、数据、结果和交付材料的架构；含模块样例与完整项目样例。
---

# 科研项目管理：动作层与结构层

一个总 skill，内部两层模块。**动作层决定怎样做，结构层决定对象放在哪里、谁维护、怎样关联与检查。两层配合使用，不能只读动作便开始写文件。** 不启动常驻 Agent，不要求每次加载全部模块。

## 开始工作的读取顺序

1. 定位用户授权的项目与目标，读实际 AGENTS、README、PROJECT；核对路径与已有约定。优化本 skill 不等于迁移案例项目。
2. 从下表选动作模块；同时加载它涉及的结构模块。创建、移动、新增目录或修改公共接口前，读对应结构正文及项目该职责区 README。
3. 先确定输出归属、权威来源、消费者与检查方式，再执行。缺少入口时，在已授权的创建／整理范围内补齐；现有项目只读接入则报告缺口，不自动搬迁。
4. 保存实际产物与证据，再回写 TASK、LOG 和必要的 FINDINGS。结构发生变化时同步相应架构说明和导航；未核对项明确标出。

## 动作层：按当前工作加载

| 当前动作 | 动作模块 | 配套结构模块 |
|---|---|---|
| 新建项目／职责区，接入旧布局，整理与迁移 | [创建与整理](modules/organize/GUIDE.md) | 整体项目＋涉及的各区 |
| 项目范围、共享依赖、开工、接续与收尾 | [project](modules/project/GUIDE.md) | 整体项目、文档 |
| 方向、方案、计划拆合、任务与进度 | [plan](modules/plan/GUIDE.md) | 文档；涉及产物时加结果 |
| 修改科研代码、配置及核对影响 | [code](modules/code/GUIDE.md) | 代码与配置；按实际 IO 加数据／结果 |
| 执行、恢复、核对作业与导入结果 | [run](modules/run/GUIDE.md) | 代码与配置、数据、结果 |
| 比较结果、形成判断及安排后续 | [interpret](modules/interpret/GUIDE.md) | 文档、结果 |
| 固定采用、研究包、交付与归档 | [release](modules/release/GUIDE.md) | 交付、结果；数据纳入时加数据 |

每个动作模块都有自己的输入→处理→输出流程和 EXAMPLE.md；这些不是项目里的七个文件夹。普通文档或代码修改无需建立分析 run。

## 结构层：按涉及的对象加载

| 对象 | 架构与约束正文 | 填写完整的样例 |
|---|---|---|
| 整体项目：代码仓、文档、数据盘与结果的关系 | [project](structures/project/GUIDE.md) | [完整项目](structures/project/EXAMPLE.md) |
| 文档：PROJECT、计划、任务、发现与历史 | [documents](structures/documents/GUIDE.md) | [文档样例](structures/documents/EXAMPLE.md) |
| 代码与配置：入口、计算模块、路径、环境、测试 | [code](structures/code/GUIDE.md) | [代码样例](structures/code/EXAMPLE.md) |
| 数据：单／多模态、raw、共享 interim、身份映射 | [data](structures/data/GUIDE.md) | [数据样例](structures/data/EXAMPLE.md) |
| 结果：结果根、run、溯源、产物、台账与归档 | [results](structures/results/GUIDE.md) | [结果样例](structures/results/EXAMPLE.md) |
| 交付：采用清单、稿件来源与固定交付包 | [delivery](structures/delivery/GUIDE.md) | [交付样例](structures/delivery/EXAMPLE.md) |

结构模块分别维护本区规则；动作模块引用，不再各写一套目录要求。跨区落点以 [归属规则](structures/project/placement-rules.md) 为准。所有样例使用合成身份和示意绝对路径，不代表真实项目已建立或验证；使用时替换成现场路径。

## 项目本身也要有架构与样例

采用本规范的项目要能从根 README／AGENTS 找到整体结构，再进入文档、代码、数据和结果各区的说明。每个实际存在的职责区在自己的 README 或已有等价入口写明：职责、真实目录树、输入输出／依赖、关键约束、一个具体使用样例、检查方式。小模块可合写一个章节，不为对称性预建空目录。

- AGENTS 保存当前整体架构与操作规则；PROJECT 登记权威资源与计划入口；各区 README 解释内部结构，导航相互引用，不复制任务状态或数据台账。
- 每份 PLAN 在目标之后、详细方案之前设“本计划资源与目录”，集中说明本计划使用的数据、代码、结果、参考资料及完整绝对路径、用途、读写边界和核对状态；不能只给项目总根或让读者翻旧对话。具体规则见文档结构模块，填写样例见 PLAN 模板与文档 EXAMPLE。
- 结果根 README 必须能定位实际数据布局、单／多模态、raw／interim 的绝对路径及数据说明入口；run 记录具体输入版本。
- 新文件先按职责归位，收尾核对受影响入口。按 [职责区 README 模板](assets/templates/area-readme.md) 填写，完整示例见结构层各 EXAMPLE。

## 共同约束与按需深入

原始数据只读；单模态默认 data/{raw,interim}，多模态默认 data/<模态>/{raw,interim}。结果独立存于已登记结果根的 runs/<run_id>，多个计划引用同一结果。输入／科学配置／代码变更产生新 run；符合恢复条件才续跑旧 run。IO 通过项目 path_manager 解析为绝对路径。

先映射旧布局，迁移与清理限定在实际授权内。文件归属、临时目录和归档遵守结构层；不得因为名字旧就删除。配置修改立即验证解析和实际生效值。版本控制遵守 jj／Git 项目规则，大于 5 MB 不入仓，见 [项目入口](structures/project/entrypoints.md)。

- 开工、执行和交付：读 [日常规范](docs/daily-operations.md)，保留四口、备份、终评准入与科学验收要求。已有授权内继续，不重复确认。
- 分析设计与结果回填：读 [结果工作流](docs/results-workflow.md)；多步骤执行与恢复：读 [执行流程](docs/snakemake-workflow.md)。
- 跨模块读写与恢复：[协作契约](docs/architecture-contract.md)；与其他流程包共用计划：[协作约定](docs/skill-interoperability.md)。
- 研究阶段、复现及证据范围：[研究原则](docs/research-principles.md)；源码接口：[共同契约](references/contracts.md) 与 [record v2](docs/record-v2.md)。
- 新项目生成与现有校验器：[模板指南](docs/template-guide.md)。模板存在、程序成功、科学有效与正式采用分开报告。

同一事实保存一处，写前重读、核对基线，保留人工解释和历史。共享产品变化检查消费者；未知和未检查不填成通过。规范正文和来源资料分开，历史稿不覆盖当前结构层。两层总览与阅读依据见 [整体架构](docs/system-architecture.md) 和 [重构依据](docs/two-layer-design.md)。
