# 计划资源入口：两个编码助手案例的改进依据

日期：2026-10-21。只读指定 PLAN 与对应会话，修改范围为 research-project skill；未修改两个案例项目。仅讨论文档和路径组织，不复核案例的科学方法、样本统计或临床结论。

## 原始证据

会话通过 <session-db> 的只读连接，按指定 session_id 读取用户与助手文本；排除工具输出和系统注入。重点核对用户要求四类目录的消息及随后目录表修改，结合当前 PLAN 正文。没有将原始个体材料复制进 skill。

- preprocessing-example PLAN：`<data-root>/<modality>/示例研究A/docs/plans/preprocessing-example/PLAN.md`；会话 `<session-id>`；关键用户消息 `<message-id>`；读取版本 SHA-256：`<sha256>`。
- metrics-example PLAN：`<project-root>/docs/plans/metrics-example/PLAN.md`；会话 `<session-id>`；关键用户消息 `<message-id>`；读取版本 SHA-256：`<sha256>`。

## 发现

两个会话均先创建了能通过结构校验的 PLAN，用户再次要求明确数据、代码、结果与参考资料之后，才补目录总表。原模板只有“输入／人群”等简述，没有把本计划资源地图作为显式组成部分。

当前案例已明显改善，但仍提示几个通用需求：参考代码与本项目实现应区分；一个计划可使用多个结果根和历史基准；参考材料可能是文件、外部仓库、历史计划或实验程序，而非单一 references 目录；声称全绝对路径的表格仍可能出现省略路径；数据根位置不能代替最终纳入范围。

## 本次决定

PLAN 目标之后设置“本计划资源与目录”，集中维护四类资源及路径、用途／读写边界、核对状态与日期，必要时多行。随后说明实际数据范围和输入→实现／配置→结果→下游关系。没有新建 PATHS／RESOURCES 或额外台账。

PROJECT 管共享根；PLAN 管本计划选择及导航；TASK 指回资源表；run／数据产品继续保存版本事实。接手时不依赖旧会话，修订时不重复维护散落路径表。交付计划必须提供实际 PLAN 链接。

模板中的未知项保持未知；路径存在不等于数据完整或结果有效。check_plans.py 仍只验证其已有身份／依赖／证据能力，不宣称已自动检查资源表。

## 相关入口

- [结构规则](../structures/documents/GUIDE.md#本计划资源与目录)
- [PLAN 模板](../modules/plan/assets/PLAN.md)
- [填写样例](../structures/documents/EXAMPLE.md#本计划资源与目录示例)

附带修正：上一轮历史快照中的 SKILL.md 被宿主重复发现为同名 skill，现保留原文并改名为 SKILL.snapshot.md，snapshot.json 记录 stored_path；只有根 SKILL.md 作为发现入口。
