# 项目工作约定

项目：{{PROJECT_ID}}
代码根：{{PROJECT_ROOT}}
架构核对日期：{{DATE}}

## 必用 skill

- 项目管理、计划、运行与结果：[research-project]({{SKILL_ROOT}}/SKILL.md)。先选动作模块，再读涉及对象的结构模块与项目职责区说明；不能只读动作便创建文件。

## 可选：按需引用你已安装的写作／版本控制 skill

下面只是示例格式，用你本机实际安装的 skill 名称替换；不需要就整段删除。

- 中文输出：`{{WRITING_ROOT}}/<your-writing-skill>/SKILL.md`
- 版本控制操作前：`{{WRITING_ROOT}}/<your-vcs-skill>/SKILL.md`

上面两行是可选占位，不是必需依赖；不把未安装的 skill 当作已加载。只修改获授权对象；优化 skill 不等于迁移案例项目。

## Superpowers 与其他流程包的文档落点

本项目使用 research-project 的文档结构。调用 brainstorming、writing-plans 或执行类 skill 前，先定位 PROJECT 登记的所属 plan；复用已有计划，不按插件调用次数新建 plan。

- 研究目标与方案：docs/plans/<plan_id>/PLAN.md。
- 设计稿：同一计划目录的 DESIGN.md；详细实施步骤：IMPLEMENTATION.md。有多项独立工作时用 DESIGN-<topic>.md／IMPLEMENTATION-<topic>.md。
- TASK.md 是任务当前状态与验收证据的唯一来源；实施文件关联 task_id，复选框仅作派生视图。LOG.md 追加执行与审查事件。
- 不另建 docs/superpowers/specs、docs/superpowers/plans 等并行记录体系。旧目录先登记，未获迁移授权不搬动。
- 将实际 design、implementation、TASK 绝对路径与身份传给执行器和审查者；切换工作区后重新解析路径。详细设计和实施文件按需生成，不预建空文件。
- 同一文档被替代的旧版本进入本计划 backup 或已保存的 jj／Git 历史；不同实施事项不是旧版本。
- 项目路径约定覆盖插件默认保存位置，保留适用的设计确认、测试与审查流程。以实际安装 skill 和工具接口为准，AGENTS 不会自动改写硬编码脚本。
- 插件示例 Git 命令按本项目 jj／Git 规则适配，不扩大提交、推送、删除或工作区操作授权。

详细兼容说明：[流程包协作]({{SKILL_ROOT}}/docs/skill-interoperability.md)。

## 当前项目架构

以下是生成时实际存在的结构；后续新增代码、配置、数据映射或计划时，在同一次变更中更新本节和路径表，填写核对日期。结构过期时先按磁盘事实核对，不把目标结构标成已经存在。

```text
{{PROJECT_ROOT}}/
├── AGENTS.md
├── README.md
├── .gitignore
└── docs/
    ├── README.md
    ├── PROJECT.md
    └── plans/{{PLAN_ID}}/
        ├── PLAN.md
        ├── TASK.md
        └── LOG.md
```

| 职责 | 实际绝对位置与状态 |
|---|---|
| 项目目标与计划入口 | {{PROJECT_ROOT}}/docs/PROJECT.md |
| 文档架构与使用样例 | {{PROJECT_ROOT}}/docs/README.md |
| 当前计划方案 | {{PROJECT_ROOT}}/docs/plans/{{PLAN_ID}}/PLAN.md |
| 任务与接续 | {{PROJECT_ROOT}}/docs/plans/{{PLAN_ID}}/TASK.md |
| 执行历史 | {{PROJECT_ROOT}}/docs/plans/{{PLAN_ID}}/LOG.md |
| 活代码与配置 | 待登记；尚未创建 |
| 数据根、raw 与 interim | 待登记；不移动原始数据 |
| 结果根与台账 | 待登记；默认结果根下 runs/<run_id>，不绑定计划 |
| conda 环境与 Python 绝对路径 | 待核对并填写 |

AGENTS 维护实际架构和操作规则；PROJECT 维护目标、边界与计划入口；TASK 维护当前状态。引用已有内容，避免复制三份进度。计划目录仅一个当前 PLAN，旧版本使用 backup/ 或已保存的版本历史。

## 结构模块与本地说明

整体规则：[project]({{SKILL_ROOT}}/structures/project/GUIDE.md)。按涉及对象读取 [documents]({{SKILL_ROOT}}/structures/documents/GUIDE.md)、[code]({{SKILL_ROOT}}/structures/code/GUIDE.md)、[data]({{SKILL_ROOT}}/structures/data/GUIDE.md)、[results]({{SKILL_ROOT}}/structures/results/GUIDE.md)、[delivery]({{SKILL_ROOT}}/structures/delivery/GUIDE.md)。创建或整理再读 [organize]({{SKILL_ROOT}}/modules/organize/GUIDE.md)。

每个实际存在的职责区要在自己的 README 或已有等价入口说明内部架构、依赖、约束、一个具体样例和检查方式。代码子模块较小时合写在 code README，复杂时独立说明；数据集保留字典与版本来源；run 使用 record/config/provenance/CHECKS，避免重复记录。

测试和探索 notebook 都归代码区，默认使用 code/tests 和 code/notebooks，不在仓库根创建同级 tests 或 notebooks；已有目录未经迁移授权不搬动。

单模态数据默认 data/{raw,interim}，多模态默认 data/<模态>/{raw,interim}。结果 README 必须包含实际输入数据树、模态、raw/interim 绝对路径和数据说明入口。新建或改变布局时同步相关说明，不等到积累混乱后再整理。

## 新文件与归档位置

先按材料职责定位，禁止为方便在仓根、docs 根或数据盘根新建零散计划和混装 archive／legacy／待清理桶。整理计划进入 docs/plans/<plan_id>/，决定归主责计划，外部参考归 references，自产发现归 FINDINGS，生成产物归 run。旧布局先映射，不自动迁移。历史 run 如获授权冷归档，只能进入登记结果根的 archive；跨盘同样适用。详细要求见 [文件归属规则]({{SKILL_ROOT}}/docs/placement-rules.md)。

## 临时文件约定

不自动在仓根、docs 根或数据盘根新建 scratch/、tmp/、temp/ 或同义杂物目录；.gitignore 的排除项不是创建授权。
运行临时文件放该 run 的 tmp/，可复用中间数据放已登记 interim；一次性调试／预览使用系统工具创建的唯一临时目录。需要保留的证据与产物归入 run；脚本和编排器归代码目录。外部集群临时存储须有实际约定并按 run 隔离。
已有临时目录先检查来源和活跃依赖，不自动迁移或删除。系统临时文件不能作为唯一证据；清理遵守授权范围，不清空共享临时目录。

## 架构同步

新增、移动、重命名目录，改变代码入口、环境、数据或结果位置，增加／归档计划时，同步本文件目录树、权威路径、相关 PROJECT 引用与 README 入口。收尾核对实际文件和链接；外部目录未访问时标未核对。这里的“实时”指随变更同步，不意味着已配置后台监控。

## 执行与数据

使用项目指定 conda 环境；不向系统 Python 安装包。IO 通过项目 path_manager 获取绝对路径；参数引用配置。修改 JSON／TOML／YAML 后立即验证解析与实际生效值。

raw 只读；命名映射与敏感信息不入仓。数据与大产物留数据盘，代码仓只保留必要文档、配置、索引和小型验证材料。每次运行隔离，保存有效配置、代码及未提交改动来源、输入与环境。现有文件不自动删除或迁移。

## jj／Git 与大小限制

- 先识别仓库。存在 .jj 时遵守 jj 工作流，不运行 git commit、push、reset、checkout 等写操作；只在普通 Git 仓库采用相应 Git 操作。
- 默认新项目建议 jj colocate；实际初始化需用户选择。不因文档整理强制初始化仓库。没有 VCS 时使用计划 backup 保存历史。
- 单个文件大于 **5 MB（5,000,000 字节）**不得进入 jj／Git；恰好 5 MB 允许。不限扩展名，小型 PDF／Office 文件也不因后缀一律排除。
- .gitignore 按路径过滤，不能表达大小阈值；已跟踪文件不会因新增 ignore 自动退出版本控制。
- jj 可能在普通命令时自动快照。新增大文件后，先执行下方只读检查，将不该纳入的文件按明确路径加入 .gitignore 或放到已登记数据位置，再运行可能快照的 jj 命令。
- 已跟踪或已暂存的大文件须停止提交，报告位置并按授权处理；不得自动删文件或重写仓库历史。DVC 指针可入仓，真实数据仍在仓外；Git LFS 不作为默认绕过大小规则的方式。

检查命令（先填写 conda Python 的绝对路径）：

```text
<conda-python> {{SKILL_ROOT}}/scripts/check_repo_files.py --root {{PROJECT_ROOT}}
```

检查支持普通 Git 和 colocated jj 的工作区候选文件及 Git 索引；非 colocated jj 或未初始化目录返回未完成检查，不冒充通过。脚本只读，不安装 hook；不是自动提交拦截器，不审计历史提交或远端对象。

## 项目命令

运行、验证、恢复的真实命令：待核对后填写。不要根据模板猜测入口；检查通过与科学验收分别报告。
