# 数据结构样例

合成项目 demo-rest 的数据盘为 /srv/research/demo-rest/storage，未实际创建或读取个体数据。

## 单模态数据 README 示例

本项目只有 EEG 数据，省略 eeg 目录层。

```text
/srv/research/demo-rest/storage/
├── README.md
├── data/
│   ├── raw/batch-01/
│   └── interim/clean-rest/v1/
│       ├── README.md
│       └── channels.tsv
└── results/README.md
```

原始区 /srv/research/demo-rest/storage/data/raw 只读。共享数据区 /srv/research/demo-rest/storage/data/interim 采用 dataset_id/version。结果入口是 /srv/research/demo-rest/storage/results/README.md；本页不复制运行台账。

使用样例：从 clean-rest/v1/README 读取生产来源、字段和单位，再通过 path_manager 获取 channels.tsv 绝对路径。消费者记录所用 v1，不扫描目录自动选最高版本。一次执行产生的新表先归该 run，需要长期复用时才登记成数据产品。

## 数据产品 README 填写示例

- 数据集：clean-rest；版本：v1；模态：EEG。
- 粒度：一行一个合成受试者的一条通道；关键字段为 subject_id、channel_id、qc_flag。QC 规则以生产配置为准。
- 来源：设计上由结果范围 /srv/research/demo-rest/storage/results 的 run_20261021_143000_qc 生产；本示例未执行，校验值未生成。
- 上游：batch-01；输入清单、配置和代码身份应从生产 run 来源记录取回。
- 权威位置：/srv/research/demo-rest/storage/data/interim/clean-rest/v1；登记为共享产品后，后续运行引用此版本；生产 run 保留来源及位置映射。
- 消费者：后续汇总运行按实际使用登记；本例尚无实际消费者。
- 检查：主键唯一、行数对应纳入通道、QC 字段值域及单位核对。当前为示例要求，未检查。

生产 run 产物转为此产品前需明确复制／移动授权，校验并切换权威引用，不让两份副本分别修改。

## 多模态变体

另一个新建的多模态项目可以采用：

```text
/srv/research/demo-multimodal/storage/data/
├── eeg/{raw,interim}/
├── fnirs/{raw,interim}/
├── beh/{raw,interim}/
└── multimodal/interim/aligned-cohort/v1/  # 有跨模态产品才创建
```

增加模态层是为了区分实际数据职责；没有 scale 就不建 scale。单模态项目后续扩展不自动搬动旧 raw，先登记映射及消费者，再决定迁移。

## 结果侧怎样查到这里

结果 README 写明“单模态 EEG、data/raw 与 data/interim”，列两个绝对路径并链接本数据 README。具体 run 另外固定 batch-01 或 clean-rest/v1 身份，避免把当前布局摘要当成历史运行的输入版本。
