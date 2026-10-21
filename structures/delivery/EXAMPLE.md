# 固定采用与交付样例

合成项目 demo-rest 的拟议交付，仅展示材料关系；当前没有真实科学验收或对外发布。

## DELIVERY 示例

位置：/srv/research/demo-rest/codebase/docs/plans/rest-qc/DELIVERY.md。
采用范围：计划将合成通道质控表及图用于流程教学；不用于临床判断。
来源范围：/srv/research/demo-rest/storage/results。
候选运行：run_20261021_143000_qc；候选产物：tables/channel-qc.tsv 与 figures/channel-qc.png。
采用状态：未采用，需实际完成运行检查、独立核对与许可／访问检查后再更新。

每项采用材料记录实际来源绝对路径、版本／哈希、用途和检查证据。不能因为本页列出候选文件就声称已有可交付包。

## 独立交付包结构示例

若用户授权准备独立教学包，可在已登记结果根的打包 run 中保存：

```text
/srv/research/demo-rest/storage/results/runs/run_20261022_100000_package/
├── record.json
├── provenance/
├── CHECKS.md
└── artifacts/teaching-package/
    ├── README.md
    ├── manifest.json
    ├── figures/channel-qc.png
    └── tables/channel-qc.tsv
```

包 README 样例：本包用于合成 EEG 质控流程展示；内部 tables 和 figures 是已选来源的固定副本；源文件身份查 manifest。复算需从来源 run 取回实际代码与环境；本设计尚未执行复算。数据均应为合成材料，发布前仍核对实际包内容。

## 操作与检查样例

固定 DELIVERY 的采用范围 → 核对源文件与检查 → 生成新包 → 逐项核对 manifest 和内容 → 保存打包 run 证据。manifest 必须来自真实文件，不能把本页当成已生成清单。

若只需在本地论文引用图，保留源 run 链接即可，不强制创建独立包。若用户只授权准备包，完成后交付本地位置；不自动上传。
