# Real-World Robots

Community real-world robot drivers, dexterous hand end-effectors, and teleoperation interfaces built on [RLinf](https://github.com/RLinf/RLinf).

See open real-world hardware tasks in [RLinf/RLinf#1943](https://github.com/RLinf/RLinf/issues/1943).

## Directory Layout

Place each robot or hardware adapter in its own subfolder:

```text
robots/<robot_name>/
├── README.md          # Hardware/SDK setup, safety notes, launch command, tested RLinf version, and demo video/logs
├── README.zh-CN.md    # Chinese README
├── requirements.txt   # Vendor SDK dependencies beyond `rlinf`
├── configs/           # Data collection, SFT, RL, or eval Hydra YAML configs
└── <module>/          # Robot/part/task adapters registered via RLINF_EXT_MODULE
```

See the [Add a Robot](https://rlinf.readthedocs.io/en/latest/rst_source/extending/new_robot.html) and [Add a Real-World Task](https://rlinf.readthedocs.io/en/latest/rst_source/extending/new_task.html) guides for RLinf's real-world robotics interface.

If your integration requires changes in core [RLinf/RLinf](https://github.com/RLinf/RLinf) (such as a new extension hook or interface update), open an issue in [RLinf/RLinf](https://github.com/RLinf/RLinf/issues) or [RLinf/RLinf-Hub](https://github.com/RLinf/RLinf-Hub/issues) to let us know.
