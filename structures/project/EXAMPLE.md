# 完整项目样例：单模态静息态研究

这是填写好的合成设计样例，未创建下面的目录，未执行分析。所有 /srv/research/demo-rest 路径均为示意绝对路径；不得直接拿来执行。本例使用一个 EEG 模态；项目、数据和运行身份在各结构样例中一致。

## 整体架构

```text
/srv/research/demo-rest/codebase/
├── AGENTS.md
├── README.md
├── .gitignore
├── environment.yml
├── code/
│   ├── README.md
│   ├── run_analysis.py
│   ├── preprocessing/clean.py
│   ├── statistics/summarize.py
│   ├── tests/fixtures/         # 小型合成输入
│   ├── notebooks/             # 有探索内容时创建
│   └── utils/{path_manager.py,config.py}
├── configs/{analysis.yaml,machine.yaml}
└── docs/
    ├── README.md
    ├── PROJECT.md
    └── plans/rest-qc/
        ├── PLAN.md
        ├── TASK.md
        ├── LOG.md
        └── FINDINGS.md          # 有观察后创建

/srv/research/demo-rest/storage/
├── README.md
├── data/
│   ├── raw/batch-01/            # 原始只读，使用合成身份
│   └── interim/clean-rest/v1/
│       ├── README.md           # 生产来源、字典、版本和检查
│       └── channels.tsv
└── results/
    ├── README.md
    ├── registry.json            # 仅已核对且显式导入的记录
    └── runs/run_20261021_143000_qc/
        ├── record.json
        ├── config_used.yaml
        ├── provenance/
        ├── logs/
        ├── tables/channel-qc.tsv
        ├── figures/channel-qc.png
        └── CHECKS.md
```

此树表示一个具备数据与运行后的目标状态，不能用它证明这些对象已经存在。新项目第一次生成仅有文档骨架；实际研究进展到相应阶段才创建其余区域。

## 根 README 的填写示例

项目 demo-rest 用于检验合成 EEG 信号的通道质控流程，不形成临床结论。代码仓为 /srv/research/demo-rest/codebase，数据盘为 /srv/research/demo-rest/storage。

阅读顺序：AGENTS 查看整体结构与操作规则；docs/PROJECT.md 查资源及 rest-qc 计划；code/README.md 查计算接口；数据盘 README 查单模态 raw/interim；results/README.md 查运行、台账和输入来源。

一次完整使用样例：读取 rest-qc 的 PLAN/TASK → 核对 batch-01 输入与 configs 的实际参数 → 由 run_analysis 入口装配清洗及汇总 → 在独立 run 保存表、图、配置和来源 → 核对 CHECKS → 把具体表格引用写回 FINDINGS。这里的步骤是设计示例，命令必须先查实际实现，未执行。

## 每个职责区的样例

| 区域 | 该项目入口 | 本 skill 的完整示例 |
|---|---|---|
| 文档 | /srv/research/demo-rest/codebase/docs/README.md | [文档结构与计划实例](../documents/EXAMPLE.md) |
| 代码及子模块 | /srv/research/demo-rest/codebase/code/README.md | [模块接口、配置和使用例](../code/EXAMPLE.md) |
| 数据与数据产品 | /srv/research/demo-rest/storage/README.md | [单模态、多模态与产品实例](../data/EXAMPLE.md) |
| 结果与单次 run | /srv/research/demo-rest/storage/results/README.md | [结果入口与来源链](../results/EXAMPLE.md) |
| 固定交付 | /srv/research/demo-rest/codebase/docs/plans/rest-qc/DELIVERY.md | [采用记录与包结构](../delivery/EXAMPLE.md) |

## 依赖关系与修改样例

batch-01 → 清洗代码＋有效配置 → run 产物 → 登记共享 clean-rest/v1 → 后续 run 引用该版本。rest-qc 计划解释结果，其他计划可引用同一产物。

新增绘图算法时：代码归 statistics 或已有绘图模块，更新 code README 的接口；新图进入新的 run，FINDINGS 引用新图；不把脚本放到数据盘，不复制原图到 docs 后独立修改。

增加 fNIRS 时：先登记新模态和旧路径，目标可采用 data/eeg/{raw,interim} 与 data/fnirs/{raw,interim}；已有 data/raw 不自动移动。只有授权迁移时更新消费者和路径映射，再同步 AGENTS、数据与结果 README。

## 完整性检查

读者应能从结果图定位生成表格、代码身份、输入批次与配置；从 TASK 找到验收依据；从数据产品找到生产 run。不存在真实运行证据时写“未执行／未核对”，不填虚构哈希或已通过状态。
