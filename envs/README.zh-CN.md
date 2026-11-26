# 仿真器与基准（Simulators & Benchmarks）

基于 [RLinf](https://github.com/RLinf/RLinf) 的社区仿真器、物理引擎后端、操作/人形评测基准、具身智能体环境以及智能体强化学习环境（GUI、代码、工具调用）接入。

开放的仿真器与基准任务见 [RLinf/RLinf#1943](https://github.com/RLinf/RLinf/issues/1943)。

## 目录结构

每个环境放在独立子目录下：

```text
envs/<env_name>/
├── README.md          # 英文说明：上游仓库、仿真器安装、启动命令、验证过的 RLinf 版本与结果
├── README.zh-CN.md    # 中文说明
├── requirements.txt   # 除 `rlinf` 之外的仿真器或基准依赖
├── configs/           # 训练或评测 Hydra YAML 配置文件
└── <module>/          # 环境封装、动作适配以及自定义 EnvWorker / 启动脚本
```

## 接入说明

`rlinf/envs/__init__.py` 中的 `SupportedEnvType` 和 `get_env_cls()` 尚未提供面向 `RLINF_EXT_MODULE` 的动态 `register_env()` 注册接口。如需在不修改核心 RLinf 的前提下接入仿真器，请在 `envs/<env_name>/` 中提供自定义 `EnvWorker` 子类或启动脚本，配套的自定义模型和算法仍通过 `RLINF_EXT_MODULE` 注册。

环境接口约定见 [新增环境指南](https://rlinf.readthedocs.io/zh-cn/latest/rst_source/extending/new_env.html)。
