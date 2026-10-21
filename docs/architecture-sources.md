# 架构资料阅读与采用记录

本页保留历次阅读和决定的演进；旧的六模块、docs/projects 和 audits 表述是历史背景。2026-10-21 当前两层重构的来源与取舍见 [本次设计](two-layer-design.md)，现行规则从 [总入口](../SKILL.md) 加载。

日期：2026-10-19。阅读对象为两个公开仓库（awesome-architecture 与 MADR），当时按本地副本选读。本轮按相关主题选读，不声称逐篇审阅整个仓库；外链、案例事实、产品宣传和模型行为概括未独立核实，也不作为本套能力承诺。

## 采用映射

- [02-架构师的思考框架.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/02-架构师的思考框架.md)：需求、约束、质量目标与取舍 → 契约第 1、5 节。
- [08-架构决策记录与演进.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/08-架构决策记录与演进.md)：接缝、决策历史、技术债与演进触发 → 第 3、6 节。
- [23-规格即架构约束怎么写给AI.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/23-规格即架构约束怎么写给AI.md)：理由、操作规则与机器检查分层 → 第 5 节，明确尚未自动化的部分。
- [24-审查清单AI产出默认缺什么.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/24-审查清单AI产出默认缺什么.md)：重复、并发、中断与按需审查 → 第 4、5 节。
- [37-共享上下文架构.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/37-共享上下文架构.md)：权威事实、来源、时效和回写 → 第 2、4 节。
- [38-AI工作流架构.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/38-AI工作流架构.md)：输入、执行、检查和回写 → 第 2、4 节。
- [39-责任与治理架构.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/39-责任与治理架构.md)：责任、授权与外部资料边界 → 第 4、6 节。
- [adr-template.md](https://github.com/adr/madr/blob/main/template/adr-template.md)：背景、驱动因素、选项、决定、后果、落实核对及关联。
- [adr-template-minimal.md](https://github.com/adr/madr/blob/main/template/adr-template-minimal.md)：保留轻量形式，不强制所有可选字段。
- [README.md](https://github.com/adr/madr/blob/main/template/README.md)：完整与最小模板的适用方式。
- [0018-use-confirmation-as-heading.md](https://github.com/adr/madr/blob/main/docs/decisions/0018-use-confirmation-as-heading.md)：Confirmation 核对决定落实，不替代科学验证。
- [0009-support-links-between-adrs-inside-an-adrs.md](https://github.com/adr/madr/blob/main/docs/decisions/0009-support-links-between-adrs-inside-an-adrs.md)：决定之间保留关系与引用。

## 取舍与本套扩展

采用清晰接口、单一事实源、故障恢复、质量场景、决策理由与落实核对。继续使用现有 Markdown 与 decisions／audits；本页记录的六个 skill 入口说法为 2026-10-19 时的沿革，2026-10-21 起已重构为一个总入口、七个动作模块与六个结构模块；无需安装 architecture-copilot、MADR 工具或新任务平台。

不照搬企业微服务、审批层级、双人审批和全量清单。已有授权内执行可逆工作；明确准入与超出授权的动作才另行确认。源文对 AI 必然遗漏或 CI 无法绕过等绝对表述不作为事实采用。

MADR 的元数据和多个章节本来可选。本套针对重要架构变更增加稳定身份、范围、迁移、恢复、落实证据与重审条件，属于本地设计，并非 MADR 原版强制要求。一般工作事件写 LOG，科学判断用既有模板；不把所有事件升级为 ADR。模板为中文改写，没有复制源仓库工具。

本次决定：保留现有目录职责，增加跨模块契约与一个 ADR 模板。替代方案为只在各入口分别增补规则；未采用，原因是接口规则会重复漂移。代价是多一份按需读取的公共文档。落实检查包括各 skill 入口校验和新增／修改文档链接检查；未部署跨文件事务、后台审计或通用架构扫描器。若将来出现机器可判定且反复发生的规则违例，再在对应项目增加针对性检查。

## 本次来源指纹

下列 SHA-256 仅标识本次读取文件内容，不代表外部事实已核实。链接指向上游公开仓库；本页不构成逐字快照。

| 文件 | SHA-256 |
|---|---|
| 02-架构师的思考框架.md | `ca6747de21cc78696495a311ff90c01598f0e0455453af9346c4a1527212adc4` |
| 08-架构决策记录与演进.md | `84892ebd8e7685443d71577620cf4615511b8d4b5058072b0cbb6662297bd0c5` |
| 23-规格即架构约束怎么写给AI.md | `f4eb949e0d8c632c1f806652a3c48634227f69562d3d3082b8bda43dd8e05410` |
| 24-审查清单AI产出默认缺什么.md | `09a96911701788bfadffa715aeb09c0707eb67b287b53e7b65e46470adc0ac76` |
| 37-共享上下文架构.md | `d29f26b9a45878e4081e9f912d794590aa320cd39497a907cb60ca6b02bea05e` |
| 38-AI工作流架构.md | `e75068083d2ce072380b5efb487ada8162e879b24c03c5cb7dc0ec379c4cba10` |
| 39-责任与治理架构.md | `431e574ff6b7c0beac3cf29a444169b13a54b1e92dd8c6446bf639f03e0b5b94` |
| adr-template.md | `940d45674563e0a2c6e96b4741b2778b18fdf0d5df1f47cc2a27a841d1b5ea82` |
| adr-template-minimal.md | `24581feeb737b4dc5603467cf9d9453b97d1784e7251f4205774a0bbc0833d90` |
| README.md | `cbee0f2c724ea78ef03cba272ff71f342faace027254ab4db75e818cdbcfdbcf` |
| 0018-use-confirmation-as-heading.md | `1a91aac93fd5afd1cb6e63fefbc0057660561926c2be6d732cb886e76b3573af` |
| 0009-support-links-between-adrs-inside-an-adrs.md | `a006a4bc2dec7280d286085d7879155a9d20c3c7806649cb85cc340931afcd26` |

## 结构修订 2 的依据与取舍

用户进一步明确要求 docs 内有 project、project 内有 plan、plan 内有 task 和 decisions。本轮据此将对象落实为目录，不再把 project 仅表达为 docs 根的 PROJECT 文件。AI 建议汇编中的自包含工作单元、协调索引和分层日志用于 project／plan／task 三层；awesome-architecture 的边界与契约用于每层输入、输出和验收；MADR 用于最小共同范围的决定与落实核对。

选择独立 TASK 的代价是文件数量增加，收益是每个任务能独立接续、验收并引用依赖。PLAN 不再复制任务状态。未采用每层都复制 findings／decisions／progress 的对称目录树：实际结果和决定仍放在能解释其完整范围的 plan 或 project。小步骤保留在 TASK 内，不递归建立子任务目录。

这是现行结构修订，取代前文“保留现有目录职责”中的物理布局；单一事实源、方向与计划多对多、共享运行和历史保留原则继续适用。只更新 skill、模板和校验器，未迁移真实项目。

## 完整工作流补充

进一步读取 awesome-architecture 第 03 章的分层图与边界说明、第 14 章的渐进迁移和架构检查段落，并复核本地 MADR 完整模板。采用分层视图、带含义的依赖箭头、可恢复变更与落实核对，未照搬服务拆分、生产数据库双写或商业案例结论。结果组织与 Snakemake 指令依据本 skill 的实际 Snakefile、run_demo.py、research_records.py 和 run.schema.json 核对，未将未来架构要求冒充已有脚本字段。

前面对话要求的完整目录树已放回总 SKILL.md；结果类型模板、产物位置、findings 回填、科学决定和采用模板通过 results-workflow.md 串联；Snakemake 的真实 DAG、前后处理、恢复与未支持范围通过 snakemake-workflow.md 串联。
