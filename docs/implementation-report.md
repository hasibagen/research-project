# research-project 首版验证记录

日期：2026-10-19。本页只记录本 skill 范围内已实测的内容；同机其他工具、其他环境下的安装与验证不在本页范围，也不在此声称。

## 已交付

本 skill 的入口 SKILL.md、内部动作模块与结构模块、共享契约、分类／回归／聚类问题模板、运行记录 JSON Schema、导入／渲染／导出程序，以及宿主展示元数据（agents/openai.yaml）。入口与模块引用同一份公共实现。

首个合成 Python demo 包含 Snakefile、两种分类规则、来源材料、自动回填与基础 RO-Crate 导出校验。一键入口为 research-project/assets/demo/run_demo.py，--output 必须是新的绝对目录。

## 实测

- 本 skill 通过 skill-creator quick_validate；展示元数据与 JSON Schema 解析通过。
- 六项程序测试通过：重复导入与冲突、篡改检测、路径越界、失败记录指标限制、人工说明保留与问题筛选、路径迁移及导出保护。
- 合成 demo 完整流程通过，validation.json 的 passed=true；验证范围为 RO-Crate 1.3 REQUIRED。报告保留了跳过项，不宣称检查了所有推荐项、外部服务可用性或科学正确性。
- recovery 演示通过先执行 data、继续下游、完成后无操作；执行入口拒绝覆盖已完成运行。此项是分阶段继续执行测试，不是强杀或断网恢复测试。
- demo 输出的 question.md 已汇总多次运行，旧结果保留，重复导入不增加行。

## 依赖

demo 需要三项第三方工具：Snakemake 9.13.7、rocrate 0.16.0、roc-validator 0.12.2。生成器、标准版本与校验器版本须成组固定并验证兼容性；工具与依赖要一起定版本，本次即为兼容既有库版本调整过依赖组合。版本未验证时只称内部记录，不声称符合某个 profile。

## 未完成范围

真实项目接入、强杀恢复、真实超算与多机并发、R/MATLAB 第二个 demo、其他 AI 宿主、Workflow Run profile、发布许可选择、开源打包及独立行为评估均未完成。当前是可使用的首版，不是全部 plan 的发布验收。未修改任何真实项目的数据或代码，未发布远端仓库。

后续文档改进：已补回日常操作检查并归并 docs；未因此增加脚本自动闸门或新的远端实测。
