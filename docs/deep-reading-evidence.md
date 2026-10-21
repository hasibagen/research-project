> 本文保留 2026-10-16 的阅读记录，属于历史证据，不直接决定当前操作。原文快照保留在本地归档（公开版不含该快照）。
>
> 后续更新（2026-10-19）：Snakemake 与 RO-Crate 已接入本地首版并实测；Aim 后置可选；Opik 明确不引入。本地材料旧称“Clary 2022”已在设计书核对为 Arguillas 等（2022），Stoudt 的正式发表年份为 2021。下文保留当时措辞以便追溯。真实超算、跨语言与其他宿主仍未验证。
>
> 阅读顺序：[日常规范](daily-operations.md) → [设计书](design-plan.md) → 本文按需查证。论文原文、工具源码和 AI 建议汇编保留原位置，通过链接定位，不批量复制进 skill。

# 统一项目管理框架：深读与工具证据

日期：2026-10-16。配套当时规划（历史引用，本地归档 `<reference-archive>/…`，公开版不含该快照）；现行设计见 [design-plan.md](design-plan.md)。本文保留阅读范围和选型依据，不另立执行规则。

## 1. 对上一轮阅读范围的更正

上一轮没有详细阅读 The Turing Way 的设计哲学。主要核对了压缩包顶层说明、若干官方网页、部分论文及项目现场。软件也主要停留在顶层介绍。因此，上轮关于“全部不引入，只补几个脚本”的选择证据不足。

本轮增加了书籍正文、论文关键论证、工具使用文档、存储与故障处理源码。没有安装或运行 Aim、Opik、Snakemake，没有登录超算和 Windows。下面的工具结论是有源码与官方文档支持的设计推荐，环境适配和收益仍须试点验证。

## 2. The Turing Way：阅读重点及改变了什么

根目录：[book/website](https://github.com/book/the-turing-way/tree/main/book/website)。

以下区分短章正文阅读与长章相关段落核对，不把目录扫描算成全文精读。

| 章节 | 阅读范围 | 提炼出的原则 | 对方案的改变 |
|---|---|---|---|
| foreword/guiding-principles.md | 短章正文 | 透明包括决定、行动和过程；尽量开放、必要时受限 | 记录要能审阅；医院数据不必为了可重复性公开 |
| foreword/background.md | 短章正文 | 降低可重复研究的操作成本；复用已有方法与工具 | 不再预设文本加自写脚本一定最轻 |
| foreword/embracing-digital-commons.md | 正文 | 共同资源需要维护、治理与可复用实践 | 公共基础件要有版本和维护入口，不能各项目复制后自行漂移 |
| foreword/emergent-strategy.md | 原则与相关论述 | 从小单元建立稳定关系，允许变化与学习 | 先检验一套通用接口；不把社区治理文字直接当 AI 自动化规范。原章标有 under review |
| reproducible-research/overview/overview-definitions.md | 正文 | 同数据同分析的重现，与稳健性、独立数据复核和推广不同 | 统一框架分别记录执行可重现性与研究有效性 |
| reproducible-research/compendia.md | 正文 | 研究包组合数据、方法、环境和文本；只读、人生成、项目生成可随生命周期改变 | 从“文件清单”转为有生命周期的研究对象 |
| communication/research-objects.md | 正文 | 研究对象在过程中增长，可关联中间产物、失败与死路 | 研究包从启动就积累，不等论文定稿才打包 |
| communication/research-objects/ro-concepts.md | 正文 | 活研究对象、快照和归档；不同类型共享对象关系 | 分析、工具、资料、报告可以用同一框架，不必同一算法树 |
| communication/research-objects/ro-implementation.md | 正文 | 研究对象有现成标准和实现生态 | 核查 RO-Crate，避免继续自定义交换格式 |
| project-design/pd-overview.md | 正文 | 临时设计、过度设计、只有最终报告都是常见问题 | 统一默认实践，又保留科学方法变化空间 |
| project-design/pd-overview/pd-overview-planning.md | 正文 | 问题、预期、资源和风险应早明确 | 统一研究计划的内容要求，而非强制五段散文 |
| project-design/pd-overview/pd-overview-methods.md | 正文 | 数据生命周期长于单项目；工具与环境影响可重复性 | 上游数据产品与下游研究项目分开，固定引用 |
| project-design/pd-overview/pd-overview-repro.md | 文档、改变与单人项目相关段落 | 单人也应考虑怎样分工、审阅和作决定 | 把全新 AI 会话视为需要明确接口的新接手者 |
| project-design/project-management-methodologies/overview.md | 正文 | 研究需要适应性；不同方法解决不同管理问题 | 知识循环允许迭代；计算执行用明确依赖；阶段准入另管 |
| reproducible-research/rdm/rdm-fair.md | 定义、实现边界与标准相关段落 | 可发现、可访问、互操作、可复用；FAIR 不等于公开 | 标准化必要元数据，权限受控数据通过引用连接 |
| reproducible-research/rdm/rdm-metadata.md | 正文 | 数据字典、来源、上下文与社区标准 | 统一通用字段，领域数据格式保留各自标准 |
| reproducible-research/rdm/rdm-elns.md | 归档、锁定、导出、自动化与标准相关段落 | 开源不自动等于互操作；导出质量与退出能力必须检查 | 工具选择增加“移走工具后还能否读记录”的验收 |
| reproducible-research/make.md | 正文 | 依赖图把重复步骤交给机器，统一入口降低接手成本 | 使用成熟工作流执行器，停止自写调度与重跑系统 |
| reproducible-research/make/make-results.md | 正文及示例 | 论文表格与正文数值可以直接接计算产物 | 报告和论文素材成为可生成产物，减少抄数 |
| reproducible-research/code-reuse/code-reuse-packages.md | 包的动机、接口、测试与模板段落 | 常用能力应该成为有版本的包 | 公共记录、校验、导出只维护一套；项目消费固定版本 |

重要来源：[研究包](https://github.com/book/the-turing-way/blob/main/book/website/reproducible-research/compendia.md)、[研究对象生命周期](https://github.com/book/the-turing-way/blob/main/book/website/communication/research-objects/ro-concepts.md)、[元数据标准](https://github.com/book/the-turing-way/blob/main/book/website/reproducible-research/rdm/rdm-metadata.md)、[ELN 的锁定与标准](https://github.com/book/the-turing-way/blob/main/book/website/reproducible-research/rdm/rdm-elns.md)。

## 3. 可重复性论文：共同原则与分歧

本轮核对了可重复性文献集全部 57 份材料的正文标题与章节，重点深入以下材料。长篇按与设计有关的章节和段落阅读，不宣称 57 篇全部全文精读。它们也不能直接等同 57 篇不同、元数据正确的论文。

| 材料 | 本轮深入内容 | 对统一框架的贡献 |
|---|---|---|
| Stoudt 等，Principles for data analysis workflows | Introduction；探索、收敛与整理阶段及转换；Box 4 Tool Development Guide | 明确区分研究者的 workflow 和电脑的 pipeline；先用已有工具；共用数据结构与框架 |
| Peng，Reproducible Research: A Retrospective | Goals；Reproducibility and Quality；Data/Code 相关论述 | 可重复性让过程能检查，但不能保证结论正确；包装成可复用产品也有维护成本 |
| Ziemann 等，The five pillars of computational reproducibility | 端到端自动化、五支柱、文档、持续验证、挑战 | 流程、环境、数据与文档共同生效；在关键接口验收，而非只记录代码 |
| Reiter 等，Streamlining Data-Intensive Biology With Workflow Systems | 工作流系统、workflow metadata、项目组织、从已有代码构建工作流 | 工作流管理是成熟基础能力，不需要每项目重复自建；但解释与备份仍是额外职责 |
| Pimentel 等，A Survey on Collecting, Managing, and Analyzing Provenance from Scripts | 来源分类、收集、存储管理与结论 | 计划来源和实际执行来源不同；版本库不自动建立输入到输出的关系 |
| Pawlik 等，A Link is not Enough | RPI 模型、原始数据、准备过程、确切输入及结论 | 数据源链接不能替代当时的分析输入；保留清洗、纳入与转表过程 |
| Bouthillier 等，Unreproducible Research is Reproducible | 方法、随机与数据变化、探索与实证讨论 | 能重跑同一数值与比较结论稳定不同；不能把最高分自动变成研究判断 |
| Devezer 等，Scientific discovery in a model-centric framework | 创新、知识多样性及结论与限制 | 统一记录不等于统一研究策略；其模型研究不能直接证明某种管理流程有效 |
| Clary 等，10 Things for Curating Reproducible and FAIR Research | Completeness、Organization 的 RO-Crate 引用、Economy、Transparency | 研究包须足以支持指定产物；删冗余维护，保留来源与限制；标准已在本地材料中出现 |
| Semmelrock 等，Reproducibility in machine-learning-based research | 工具与平台、标准化评估、障碍与措施映射 | 代码、数据、日志、pipeline 是不同能力；RO-Crate 可以跨领域；一个平台不包治全部问题 |
| Hoffmann 等，Multiplicity of analysis strategies | Reduce/Report/Integrate/Accept uncertainty 与研究建议 | 搜索过程和替代分析要可见，不能只保存赢家；探索与确认分开 |
| Noble；Sandve；Wilson | 上轮已读的研究笔记、生成过程、随机性和足够好的计算实践，本轮作对照 | 保留最小有效记录与研究含义，避免把工程记录当科学解释 |
| Kasif；Degen；AutoResearch 预印本 | 上轮及本轮对照的主张来源、工作流选择、执行与验证边界 | 支持事实到主张的追溯；不将预印本观点当正式管理标准 |

这些材料的共同点是：对象要完整、关系要显式、流程尽量可执行、环境和数据要固定、解释必须有来源。它们没有得出“只要用纯文本就不需要工作流工具”的结论，也没有要求所有研究采用完全相同的算法。

文献质量提醒：一条以 sandve_2013__replication… 命名的条目，正文实际是 Noble；另一条条目的正文标题与标称可重复性主题不符。另有同一作品的不同版本或转换件。上述异常没有修动，推理按实际正文核对；不能把条目名当文献身份保证。

关键阅读入口（正式发表版本）：

- [研究工作流原则](https://doi.org/10.1371/journal.pcbi.1008770)。
- [五支柱](https://doi.org/10.1093/bib/bbad375)。
- [FAIR 研究包整理](https://doi.org/10.15497/RDA00074)。
- [脚本来源综述](https://doi.org/10.1145/3311955)。
- [链接不够](https://doi.org/10.1007/s13222-019-00317-8)。

## 4. 第四轮 AI 建议：保留什么，驳回什么

来源：第四轮建议汇编（本地归档 `<reference-archive>/…`，公开版不含该快照）。本轮重新核对各回答中与框架、判断、矩阵、工具和跨机有关的实质段落，重复用户提示词不作独立证据。

| 建议类型 | 可取处 | 需要纠正的地方 |
|---|---|---|
| WORKSPACE + 矩阵 + 待办 | 当前认识和累计结果要有明确入口 | 最新 commit 不决定科学判断正确；多机器并非天然同一状态 |
| 自动结果矩阵 | 指标无需人抄 | AUC/r 混排、按最高值自动 CURRENT_BEST 会误导 |
| 判断账驱动视图 | 比收尾重写总结合理 | 支持/排除一个词太少，必须保留范围、证据和限制 |
| 未打牌挂来源 | 能防跨会话遗忘 | 优先级不等于证据强度；暂缓、取消和受阻不能被删除后消失 |
| 纯文本科研操作系统 | 重视可读、可归仓与退出能力 | 这是建议者的组合命名，不是现成统一标准；不能用它排除成熟执行器 |
| “50 行脚本搞定” | 追求低维护成本 | 忽略多格式、故障、并发、幂等和科学口径，规模承诺没有证据 |
| 所有项目五类文档 | 提供了几个有用阅读视角 | 没有共同对象、接口和软件复用，仍会逐项目自定义 |

本轮采用共同的事实、判断、行动分工，拒绝把建议中的文件名和未经验证的自动判断当标准。

## 5. 软件：本轮读到了机制与源码

软件仍以 zip 形式存在，除 The Turing Way 外未解压安装。以下成员路径均位于 <toolbox>/项目管理 对应压缩包内。

### Aim

核对 docs/source/understanding/concepts.md、data_storage.md；using/manage_runs.md、configure_runs.md、remote_tracking.md；quick_start/convert_data.md；aim/cli/runs/commands.py；aim/sdk/run.py 与 setup.py 相关部分。

观察：Run 可存参数、指标与 context；一个脚本可建多个 Run；.aim 使用 RocksDB 和 SQLite；远程追踪需要可连接的服务端；已有 run hash 可以重新打开；源码提供 runs cp。不是一堆可随意并发同步的 JSON 文件。

尤其 configure_runs 明确：3.13 起不能随便用自定义字符串创建 run_hash。故公共导入器必须保存“项目现有 run/结果行 → Aim 自动生成 hash”的映射，不能写一个看似确定的自造 hash 就宣称幂等。终端日志默认采集，系统参数采集可选；本方案先只导入明确允许的研究摘要。

设计判断：推荐作为 ML 与统计比较的本地浏览层试点。批算机产通用结果，本机统一导入，避免每台机器都维护 .aim。实时追踪是后续可选能力，不是计算成功的依赖。

官方核对：[Manage runs](https://aimstack.readthedocs.io/en/latest/using/manage_runs.html)、[Configure runs](https://aimstack.readthedocs.io/en/latest/using/configure_runs.html)、[CLI](https://aimstack.readthedocs.io/en/latest/refs/cli.html)。这些是查阅到的 3.x 文档，安装时应固定可验证版本，不直接采用下载的 main。

### Snakemake

核对 docs/snakefiles/modularization.rst、configuration.rst、best_practices.rst、reporting.rst、deployment.rst；docs/executing/executors.rst、provenance.rst；rules.rst 中 R、shell、失败、资源和输出检查相关段落。

观察：支持复用 module、wrapper、配置；机器资源通过 profiles 和 executor 管理；有 Slurm 插件；shell 可调用其他语言；可生成包含拓扑、运行统计和来源的报告。原生追溯默认保存在 .snakemake/metadata；另有实验性数据库后端，本方案不以切换该后端为前提。

官方 Windows 指引是 WSL，不能承诺 Windows 原生 MATLAB 与 Linux 工作流直接无缝。归档功能可能收集输入文件，不能直接把它当医院数据的发布导出器。失败保留、禁止自动删原件、封存结果不覆盖等仍需在公共工作流约定中落实。

设计判断：推荐作为多阶段计算的默认编排器，先试一条 MATLAB→R/Python 链。示例医院单体运行器先整段调用，确认科学等价后再按计算单元拆。不要为用 Snakemake 重写折内算法。

官方核对：[模块复用](https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html)、[配置](https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html)、[报告](https://snakemake.readthedocs.io/en/stable/snakefiles/reporting.html)、[Slurm executor](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/slurm.html)、[Windows 安装边界](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html)。

### Opik

核对 self-host/architecture.mdx、local_deployment、backup；tracing/advanced/offline_fallback.mdx；evaluation/concepts.mdx、advanced/manage_datasets.mdx、export_experiment_results.mdx；SDK replay/db_manager.py 与 shutdown 测试的相关部分。

观察：数据集、任务和指标适合比较提示词与模型；可导出实验结果；自托管涉及应用服务和多个数据服务。Python SDK 有离线 fallback，但源码使用临时目录，关闭过程会清理临时资源；不能据“离线缓存”四个字承诺断网退出后永久归档。该快照还带有 shutdown replay 的回归测试，不据此认定发布版仍有同一 bug。

设计判断：推荐在 Meta 提取、核验、提示词比较等 LLM 工作线上做专用试点，使用实际金标准和确定性检查。研究原始记录先持久落地，Opik 是追踪评估工具；不要把 LLM judge 分数直接当正确提取或科学成立。也未证实它能自动完整接管其他编码助手、Claude Code、Codex 三个交互会话。

官方核对：[架构](https://www.comet.com/docs/opik/self-host/architecture/)、[本地部署](https://www.comet.com/docs/opik/self-host/local_deployment/)、[离线回放](https://www.comet.com/docs/opik/tracing/advanced/offline_fallback/)、[实验导出](https://www.comet.com/docs/opik/evaluation/advanced/export_experiment_results/)。

### 其他本地候选

补查 Calkit 的 docs/pipeline/index.md，确认其 DVC 管线依赖；查 ClearML Task 的 offline 相关实现和 W&B Settings 的 offline 模式；查 Nextflow README 与 data-lineage ADR。

这些观察说明它们各有可用能力，但没有证明比 Snakemake + Aim 更适合本轮目标。Nextflow 是同层替代候选，不应同时推广两套默认编排器；ClearML/W&B 是追踪替代候选，不应与 Aim 建三套并行实验库；Calkit 的依赖与原有 DVC 约束仍冲突。

## 6. 为什么补查 RO-Crate 与 PROV

这不是为了再增加一个平台。The Turing Way 的研究对象章节，以及本地 Clary、Semmelrock 材料都指向标准化的研究包和来源表达。若要避免各项目各写出生证格式，必须核对现成标准。

[W3C PROV](https://www.w3.org/TR/prov-overview/)提供实体、活动、责任者及其来源关系。[RO-Crate](https://www.researchobject.org/ro-crate/)提供研究资源与元数据的打包方式。[Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/profiles/)区分不同运行记录粒度；[Process Run Crate](https://www.researchobject.org/workflow-run-crate/profiles/process_run_crate/)也能描述没有显式工作流引擎的工具执行。

推荐只从少量稳定字段与最小适用 profile 开始。研究判断和优先级仍需小规模扩展；这部分不冒称标准已经定义。未通过 profile 校验的导出不写“完全符合”。RO-Crate 不等于远程托管服务，也不要求把敏感原件公开或搬进仓库。

## 7. 尚待试点验证

Aim 在独立 conda 环境里的兼容性、导入幂等与恢复；Snakemake 对 Windows MATLAB 的桥接、HPC 控制进程生存及断线对账；Opik 的版本、资源负担、失败导出和真实评估增益；RO-Crate 生成与所选 profile 校验；两个不同项目能否不修改基础框架完成接入。

这些是工具采用的实际验收项目。本轮未安装软件，因此不会用“能用”“已打通”替代“文档与源码支持，尚待环境验证”。
