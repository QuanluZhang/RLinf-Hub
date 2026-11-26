# 模型（Models）

基于 [RLinf](https://github.com/RLinf/RLinf) 的社区具身与智能体模型接入，覆盖 VLA policy、世界动作模型（WAM）、世界模型后端、推理与多模态 LLM/VLM 以及 reward/value 模型。

开放的模型任务见 [RLinf/RLinf#1943](https://github.com/RLinf/RLinf/issues/1943)。

## 目录结构

每个模型放在独立子目录下：

```text
models/<model_name>/
├── README.md          # 英文说明：论文/权重链接、安装步骤、启动命令、验证过的 RLinf 版本与结果
├── README.zh-CN.md    # 中文说明
├── requirements.txt   # 除 `rlinf` 之外的模型额外依赖
├── configs/           # SFT、RL 或评测 Hydra YAML 配置文件
└── <module>/          # 通过 RLINF_EXT_MODULE 注册的模型 builder 与 policy 封装
```

## 注册接口

在 `RLINF_EXT_MODULE` 入口模块的 `register()` 中调用 `rlinf.models` 的 `register_model(model_type, builder, category=...)` 与 `rlinf.config` 的 `SupportedModel.register(...)`。详见 [新增模型指南](https://rlinf.readthedocs.io/zh-cn/latest/rst_source/extending/new_model_fsdp.html)。

如果接入过程需要修改核心仓库 [RLinf/RLinf](https://github.com/RLinf/RLinf)（例如新增扩展接口或调整已有约束），欢迎在 [RLinf/RLinf](https://github.com/RLinf/RLinf/issues) 或 [RLinf/RLinf-Hub](https://github.com/RLinf/RLinf-Hub/issues) 提交 issue 告知我们。
