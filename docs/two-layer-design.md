# 动作层与结构层重构：设计、依据和验收

日期：2026-10-21。范围仅为当前 research-project skill；不修改用户案例项目、外部参考资料或全局配置。用户确认采用一个总 skill、内部两层模块。

## 问题与目标

原六个入口按动作分类，结构规则散落 docs，创建新代码、文档或结果时容易跳过；整体总览还残留旧目录语义。目标是让“创建之前确定归属”进入每次动作，并让 skill 与实际项目都具备整体架构、区内架构和具体样例。

## 选项与决定

1. 只加整理动作：能处理已有混乱，不能防止其他动作继续绕过结构约束。
2. 只按文档／代码／数据／结果拆模块：对象规则清楚，但跨对象执行、判读和接续流程会分散。
3. 保留动作层，增加结构层并绑定读取：采用。一个总入口，七个动作模块，六个结构模块；每个模块有流程或结构、边界与 EXAMPLE。

代价是多了按需阅读的模块文件；通过短总入口、动作依赖表和单一规则正文限制重复。没有拆成多个独立安装 skill，没有引入新平台或后台架构服务。

## 文件与职责变更

原结构文档迁入 structures；docs 旧路径保留兼容跳转。组织动作新增 modules/organize，其余动作保留已有科学流程并增加结构依赖和样例。代码与交付结构补齐。结构样例共用 demo-rest 身份，整体项目链接逐区样例。

项目实例中，根 AGENTS／README 管整体入口，各职责区 README 管内部架构和样例；小模块合写章节。数据集与 run 继续使用自身来源记录，避免重复填写。新建文档骨架增加 docs/README，生成器函数与 CLI 保持兼容。

## 深入阅读与采用边界

读取上游仓库的本地副本，不声称与仓库最新文本一致；来源中的企业系统、模型能力或 CI 绝对表述不作为本 skill 的能力承诺。下列架构是结合用户要求的设计，不是资料规定的唯一目录标准。

| 来源 | 阅读范围 | 本次采用 |
|---|---|---|
| [03-读懂与画好架构图.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/03-读懂与画好架构图.md) | 前 180 行：边界、分层视图与依赖含义 | 整体项目与职责区分别展示；目录树不冒充运行容器图 |
| [23-规格即架构约束怎么写给AI.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/23-规格即架构约束怎么写给AI.md) | 前 180 行：决策理由、AGENTS 约束与可检查规则 | 写入前加载结构，项目入口同步；不宣称文档等于强制拦截 |
| [37-共享上下文架构.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/37-共享上下文架构.md) | 前 150 行，重点复核前 100 行：事实源、接口和回写 | 结构正文唯一，旧路径跳转，项目本地 README 提供可定位上下文 |
| [14-演进与拆分大型系统.md](https://github.com/study8677/awesome-architecture/blob/main/tutorial/14-演进与拆分大型系统.md) | 前 100 行：渐进替换与兼容边界 | 保留动作接口、脚本接口及历史快照；先替换结构读取入口 |
| [compendia.md](https://github.com/book/the-turing-way/blob/main/book/website/reproducible-research/compendia.md) | 结构示例、Methods/Data/Output 分类、创建与使用部分 | 按职责分代码／数据／结果；完整项目和区内样例帮助接手 |
| [pd-overview-repro.md](https://github.com/book/the-turing-way/blob/main/book/website/project-design/pd-overview/pd-overview-repro.md) | 最小文档、计划过程与协作准备部分 | 实际项目也保留入口和样例，不仅 skill 有目录图 |
| [adr-template-minimal.md](https://github.com/adr/madr/blob/main/template/adr-template-minimal.md) | 最小模板全文 | 记录问题、选项、取舍及代价，不另引入决策平台 |

### 本次来源指纹

用于标识本次读取的版本，不代表外部事实核验。

- 03-读懂与画好架构图.md：`9cc9b2f167c9a0de61ba83c101f9a9ac880afbc99780987723ed8bb7dc9f9116`
- 23-规格即架构约束怎么写给AI.md：`f4eb949e0d8c632c1f806652a3c48634227f69562d3d3082b8bda43dd8e05410`
- 37-共享上下文架构.md：`d29f26b9a45878e4081e9f912d794590aa320cd39497a907cb60ca6b02bea05e`
- 14-演进与拆分大型系统.md：`5af7b2a2cea8ebd5326fdba4951d73ca676dbaadd034ee8a7b1cdf1cfeb9205f`
- compendia.md：`f797eb55b84ddc1def17948294c40f5e0d991ebd859b684807a72bdf5d605398`
- pd-overview-repro.md：`e79ee1830596bfefa07e0ac9f7a2e9ec8fc4aacf1954b92f0a6772747426c9aa`
- adr-template-minimal.md：`24581feeb737b4dc5603467cf9d9453b97d1784e7251f4205774a0bbc0833d90`

## 保留的约束

原始数据只读、单模态简化、多模态分层、run 独立于计划、代码与配置溯源、四口／备份／终评准入、科学验收、5 MB 限制、jj 规则及禁止未授权删除继续适用。配置修改后验证生效。已有布局先映射，结构规范不授权自动迁移。

## 验收范围

检查根入口能分别到达动作和结构，七个动作均能定位相应结构及例子，六个结构都有完整样例；核对链接、旧入口跳转、生成骨架与声明一致，并运行原有计划／记录／模板测试。行为核对使用新建单模态、修改配置、运行恢复、结果判读和旧布局整理等场景。

实际测试结果另见 [本次验证记录](two-layer-validation.md)。模板和例子均不代表真实研究执行或科学有效，未新增自动全盘架构检查器。

## 历史与恢复

重构前的 Markdown／Python 文件快照与 manifest 保留在本地归档（公开版不含该快照）。该归档只作历史依据，不作为当前规范；恢复必须先核对后续改动，不能直接覆盖现场。上游公开来源保持原样。
