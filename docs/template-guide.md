# 文档模板使用

使用 conda Python 运行 scripts/create_project_template.py --help。生成器仅写尚不存在的绝对目录，不修改已有项目或初始化仓库。

```text
<conda-python> <skill>/scripts/create_project_template.py --output <new-absolute-dir> --project project-a --plan baseline-study --task baseline
```

默认生成 AGENTS.md、README.md、.gitignore、docs/README.md、docs/PROJECT.md 与 docs/plans/{plan}/PLAN.md、TASK.md、LOG.md。按真实项目填写负责人、数据、环境、方案与权限；模板通过机械检查不表示科学设计已审阅。

PLAN 在目标之后自带“本计划资源与目录”：四类资源、绝对路径、用途／权限、核对状态以及数据范围和资源关系。生成时仍是待填写项；落地计划须据实际资料补齐。check_plans.py 不检查该表，不能把校验通过说成资源已核实。具体样例见 [计划资源表](../structures/documents/EXAMPLE.md#本计划资源与目录示例)。

需要运行目录教学样板时加 --with-run-template，才生成 results-templates/run-template。它不是实际 run，record.template.json 的哈希故意无效，不能导入。

## 按需资源

- 研究发现：assets/templates/analysis.md → 计划内 FINDINGS.md；多个独立问题再拆 findings/，结合 analysis-types.md。
- 决定：scientific-decision.md 或 architecture-decision.md → 计划内 decisions/；使用真实证据与范围。
- 正式交付：release.md → 计划内 DELIVERY.md，固定采用来源；不自动创建 releases。
- 详细检查：audit.md、reproduction-check.md 为可选报告，任务链接报告；不自动创建 audits。
- progress.md、project-index.md、plan-index.md 保留兼容旧项目，不是默认生成清单。

PROJECT 内维护计划入口；状态以 TASK、PLAN 为准。check_plans.py 用绝对 --root 和 --plans（docs/plans）校验身份、依赖及证据，兼容旧结构。资料只有需要时创建目录；完成计划不搬动。具体职责以 [结构规范](../structures/documents/GUIDE.md) 为准。

历史计划归档用 plan-backup-index.md 填写计划 backup/README.md；数据盘入口用 data-root-readme.md。二者均按实际需要启用，不默认创建空目录或迁移已有项目。

AGENTS、README 和 ignore 模板及大小门槛见 [项目入口规范](../structures/project/entrypoints.md)。生成器不会初始化仓库、安装提交 hook 或扫描其他项目。

项目整理使用 [整理方案正文模板](../assets/templates/structure-adoption-plan.md)，放在所属 plan 的 PLAN 中，任务状态在 TASK；文件落点按 [归属规则](../structures/project/placement-rules.md) 检查。


## 两层架构与项目实例

创建或整理先读 [organize](../modules/organize/GUIDE.md)，然后选择相应结构模块。结构层 GUIDE 提供规则，EXAMPLE 提供填写完整的合成实例；完整项目从 [项目实例](../structures/project/EXAMPLE.md) 阅读。

生成器现在同时生成 docs/README.md，说明真实文档树和当前计划的读写样例。代码、数据、结果等区由实际任务按需建立，不因生成器返回成功就声称整个科研项目已实现。

每个新建职责区用 [区 README](../assets/templates/area-readme.md) 记录架构与样例；数据／结果优先用各自专用 README 模板。独立代码子模块可设自己的 README，较小模块合写。结果入口必须能定位数据布局，具体输入版本仍在 run 来源记录维护。
