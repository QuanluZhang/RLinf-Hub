# 算法（Algorithms）

基于 [RLinf](https://github.com/RLinf/RLinf) 的社区强化学习与后训练算法实现及论文复现，覆盖 flow/diffusion RL、离线到在线 VLA RL、人形控制 RL 和 agentic RL。

开放的算法任务见 [RLinf/RLinf#1943](https://github.com/RLinf/RLinf/issues/1943)。

## 目录结构

每个算法放在独立子目录下：

```text
algorithms/<algorithm_name>/
├── README.md          # 英文说明：论文链接、安装步骤、启动命令、验证过的 RLinf 版本与曲线/日志
├── README.zh-CN.md    # 中文说明
├── requirements.txt   # 除 `rlinf` 之外的额外依赖（如有）
├── configs/           # Hydra YAML 配置文件
└── <module>/          # 通过 RLINF_EXT_MODULE 注册的 advantage、loss 或 worker 模块
```

## 注册接口

在 `RLINF_EXT_MODULE` 入口模块的 `register()` 中调用 RLinf 注册表：

- `rlinf.algorithms.registry` 中的 `@register_advantage("<name>")`
- `rlinf.algorithms.registry` 中的 `@register_policy_loss("<name>")`
- `rlinf.algorithms.rewards` 中的 `register_reward("<name>", cls)`

如果接入过程需要修改核心仓库 [RLinf/RLinf](https://github.com/RLinf/RLinf)（例如新增扩展接口或调整已有约束），欢迎在 [RLinf/RLinf](https://github.com/RLinf/RLinf/issues) 或 [RLinf/RLinf-Hub](https://github.com/RLinf/RLinf-Hub/issues) 提交 issue 告知我们。
