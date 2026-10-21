# 结果结构及运行样例

与完整项目共用合成身份；本页说明一个未来执行后的布局，不代表实际运行成功。

## 结果 README 示例

结果根：/srv/research/demo-rest/storage/results。执行范围为本结果根，run_id 在此范围内唯一。计划可引用结果，不以计划名分割结果所有权。

```text
/srv/research/demo-rest/storage/results/
├── README.md
├── registry.json
└── runs/run_20261021_143000_qc/
    ├── record.json
    ├── config_used.yaml
    ├── provenance/
    │   ├── inputs.json
    │   ├── environment.txt
    │   └── code.patch            # 有未提交改动时保存
    ├── logs/
    ├── tables/channel-qc.tsv
    ├── figures/channel-qc.png
    └── CHECKS.md
```

输入数据是单模态 EEG：raw 为 /srv/research/demo-rest/storage/data/raw，interim 为 /srv/research/demo-rest/storage/data/interim。数据架构与来源入口是 /srv/research/demo-rest/storage/README.md。run 的具体输入取 record 及 provenance，不从本页推定。

## 单次 run 的内部架构与样例

本次设计输入为 batch-01，入口是 /srv/research/demo-rest/codebase/code/run_analysis.py，有效配置保存在本 run 的 config_used.yaml。provenance 记录输入清单、代码身份、环境和实际需要的随机性；它们按真实 schema 接口关联，不凭示意字段修改 record schema。

channel-qc.tsv 保存计算事实，channel-qc.png 由该表生成；CHECKS 核对通道计数、单位、异常位置与产物身份。LOG.md 只写关键事件，完整机器日志在 run/logs。临时文件需要时创建 run/tmp，不写数据盘根 tmp。

查找样例：从 registry 定位完整运行身份 → 打开 record → 校验表图和来源 → 查看 CHECKS → 查 rest-qc/FINDINGS 的解释。没有记录导入时说明未登记，不把文件存在当成台账已有。

## 变更、复用与汇总

调整质控阈值时新建 run，例如 run_20261021_160000_qc；旧表保留。后续比较产生新表或图则建汇总 run，登记这两个来源。仅补充文字解释直接写 FINDINGS。

需要跨计划复用 clean-rest/v1 时按数据产品规范登记，不把整个 run 复制进两个计划目录。校验输入、配置和代码完全一致且程序支持断点恢复时，才沿用原 run 并另存恢复日志。

本页中的 filenames 与身份是结构样例；有效 record 应由真实执行证据按 [记录接口](../../docs/record-v2.md) 构造，不能使用虚构哈希导入。
