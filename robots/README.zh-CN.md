# 真机机器人（Real-World Robots）

基于 [RLinf](https://github.com/RLinf/RLinf) 的社区真机机器人驱动、灵巧手末端执行器与遥操作接口接入。

开放的真机硬件任务见 [RLinf/RLinf#1943](https://github.com/RLinf/RLinf/issues/1943)。

## 目录结构

每个机器人或硬件适配放在独立子目录下：

```text
robots/<robot_name>/
├── README.md          # 英文说明：硬件与 SDK 安装、安全说明、启动命令、验证过的 RLinf 版本与演示视频/日志
├── README.zh-CN.md    # 中文说明
├── requirements.txt   # 除 `rlinf` 之外的厂商 SDK 依赖
├── configs/           # 数据采集、SFT、RL 或评测 Hydra YAML 配置文件
└── <module>/          # 通过 RLINF_EXT_MODULE 注册的机器人、零部件与真机任务适配
```

真机接口与任务接入规范见 [新增机器人指南](https://rlinf.readthedocs.io/zh-cn/latest/rst_source/extending/new_robot.html) 和 [新增真机任务指南](https://rlinf.readthedocs.io/zh-cn/latest/rst_source/extending/new_task.html)。

如果接入过程需要修改核心仓库 [RLinf/RLinf](https://github.com/RLinf/RLinf)（例如新增扩展接口或调整已有约束），欢迎在 [RLinf/RLinf](https://github.com/RLinf/RLinf/issues) 或 [RLinf/RLinf-Hub](https://github.com/RLinf/RLinf-Hub/issues) 提交 issue 告知我们。
