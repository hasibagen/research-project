# 八项建议与模板完善：落实记录

2026-10-19。用户转述的外部体检作为改进建议，不视为已验证的现场事实；未操作其他编码助手链接或其他项目。

| 建议 | 落实 | 自动化范围 |
|---|---|---|
| 科学值域、计数与容差 | results-workflow 最小科学健全性检查；结果类型模板 | 领域约束由项目代码实现，公共记录只做通用有限数检查 |
| 随机稳定性 | daily-operations、analysis、analysis-types | v2 保存随机性设计；不自动认定重复次数充分 |
| 机器与环境字段 | v2 machine、randomness；v1 保留 | schema 验证、引用必须入 artifacts、哈希检查 |
| 跨平台 ID | 结构规范与模板生成器 | 生成器拒绝大写、空格、保留名；历史 ID 不强迁 |
| 模块样板去重 | 重复架构与交接段落集中到总入口／契约 | 模块保留本模块动作，链接核对 |
| 故障演练 | fault_demo.py 与测试 | 真实子进程在导入后被终止，恢复、重放、冲突及待解释断言 |
| 制度反馈 | audit 模板的规范本身问题 | 人工评价成本与缺漏，不自动改全局规则 |
| 数据保存与权限 | PROJECT 模板 | 年限与协议由用户实际材料填写，不编造年限 |

## 科学依据与措辞边界

[The Turing Way testing-exceptions](https://book.the-turing-way.org/reproducible-research/testing/testing-exceptions/) 支持对科学代码的异常情形、随机性和浮点比较作明确测试。量表上限必须来自实际数据字典；用户转述的特定项目异常未在本轮读取个体数据核实。

[Bouthillier 等（2019）官方论文入口](https://proceedings.mlr.press/v97/bouthillier19a.html) 区分复现含义并讨论实验设计。本轮采用对随机来源做稳定性检查的本地规则，不将“所有模型换 seed 必定翻转排名”归为论文普遍结论。Isdahl／Milner／CDRI 的具体引文未在本轮独立全文核对，不伪造支持段落或保存年限。

## 实测

公共记录与新增 v2／模板／故障测试共 13 项通过，计划测试 15 项通过，共 28 项。v2 合成 Snakemake 全流程重新执行成功，基础 RO-Crate 校验通过；额外运行故障演练成功；模板实例的计划校验通过。71 个当前入口与工作流本地链接存在，skill 和两个 schema 校验通过。

- [skill 内的项目模板说明](../assets/templates/project-scaffold/README.md)
- 生成器实测实例：<template-example>/（用于验证，不作为 skill 模板源）
- v2 演示回填：`<demo-output>/question.md`
- 故障演练报告：`<fault-demo-output>/fault-report.json`

故障实测范围为导入后、回填前的本地进程终止，不代表断电、磁盘损坏或远端故障均通过。生成器只创建新输出目录，遇到既有目录拒绝；没有迁移真实项目，没有把占位模板当研究证据。
