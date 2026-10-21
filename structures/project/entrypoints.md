# 项目入口、默认模板与版本控制

## 默认资源

| 文件 | 模板 | 职责 |
|---|---|---|
| 仓根 AGENTS.md | [AGENTS 模板](../../assets/templates/project-scaffold/AGENTS.md) | skill、实际架构、路径、命令、操作与 VCS 规则 |
| 仓根 README.md | [README 模板](../../assets/templates/project-scaffold/README.md) | 人类阅读入口、目的、启动与文档导航 |
| 仓根 .gitignore | [ignore 模板](../../assets/templates/project-scaffold/gitignore) | 按路径排除数据、结果、缓存、秘密和机器日志 |
| docs/README.md | [文档入口模板](../../assets/templates/project-scaffold/docs-readme.md) | 文档内部架构、读写样例与导航 |
| docs/PROJECT.md | [项目模板](../../assets/templates/project-contract.md) | 目标边界、计划入口、资源和路径 |
| 计划 PLAN.md | [方案模板](../../modules/plan/assets/PLAN.md) | 方案、范围、整体完成标准 |
| 计划 TASK.md | [任务模板](../../modules/plan/assets/TASK.md) | 当前任务、状态、证据和接续 |
| 计划 LOG.md | [日志模板](../../assets/templates/work-log.md) | 关键事件历史；不增建根 LOG 副本 |

新目录由 create_project_template.py 实例化；已有项目先读取并合并人工规则，不覆盖入口或自动初始化 jj／Git。现有根 LOG 历史按授权保留或映射，不能静默删除。数据盘与结果根有各自 README 模板，只有实际建立对应根时才填写。

## AGENTS 必须覆盖

包含 research-project 的实际 skill 链接及适用情境。其他写作与版本控制 skill 按需引用，示例名称见 [AGENTS 模板](../../assets/templates/project-scaffold/AGENTS.md)，用不到就整段删除。写作 skill 按任务加载，不宣称已加载不存在的文件。生成器使用当前用户 .agents/skills 路径，换机器先核对。

AGENTS 保存当前实际目录树、代码／配置／数据／结果／环境绝对路径与核对日期。结构变化同一轮同步；未落地目录标待创建，外部路径未检查标未核对。PROJECT 保留目标和入口，任务状态在 TASK，不把实时架构更新变成重复进度记录。“实时”不表示后台监控。

## 超过 5 MB 不入版本库

阈值为 5,000,000 字节，严格大于才拒绝。不按文件扩展名代替大小判断。Git 与 colocated jj 使用 .gitignore，但它不能按大小过滤，也不影响已经跟踪的文件。

使用 conda Python 调用 scripts/check_repo_files.py --root <仓库绝对路径>。脚本只读检查未忽略的工作区候选文件、已跟踪文件，以及 Git 暂存 blob（防止暂存大文件后工作区缩小而漏检）。Git 子模块只记录提交，不扫描子模块内部；各子模块须独立检查。符号链接按 Git 的链接内容处理，不沿链接读取外部数据。

普通 Git 与 colocated jj 可检查；未初始化目录或非 colocated jj 明确返回未完成，不宣称通过。脚本不审计历史对象、远端或安装 hook，不是强制服务端拦截器。检查和提交之间仍可能出现新修改，提交前须重新核对发生变化的文件。

jj 可能在普通操作时自动快照，新增文件后应先用只读检查器检查，补具体 ignore 路径后再进行可能快照的操作。超过阈值的文件保留在数据盘／结果根等登记位置，文档保留引用；不得自动删除文件、重写历史或通过 LFS 绕过规则。DVC 管理时入仓的是指针与元数据，真实数据另存。

本规则覆盖 project-init 旧模板中的 1 MB 示例；不修改全局 skill 或 Git 配置。没有版本库时可用 backup 保存计划历史，待用户选择是否初始化后再执行；生成文档不等于已经启用版本控制。

## 流程包兼容

AGENTS 模板包含 [Superpowers 协作规则](../../docs/skill-interoperability.md)：DESIGN、IMPLEMENTATION 归入所属计划，TASK 独立维护唯一当前状态。新增文件仍需同步架构；不修改插件安装或自动迁移既有项目。

各实际职责区的架构、约束与样例要求见 [整体结构](GUIDE.md)。生成器只创建文档骨架；新建 code/data/results 时填对应 README，已有入口满足职责时复用。
