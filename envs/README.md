# Simulators & Benchmarks

Community simulator, physics backend, manipulation/humanoid benchmark, embodied-agent, and agentic RL environment (GUI, coding, tool-use) integrations built on [RLinf](https://github.com/RLinf/RLinf).

See open simulator and benchmark tasks in [RLinf/RLinf#1943](https://github.com/RLinf/RLinf/issues/1943).

## Directory Layout

Place each environment in its own subfolder:

```text
envs/<env_name>/
├── README.md          # Upstream link, simulator setup, launch command, tested RLinf version, and results
├── README.zh-CN.md    # Chinese README
├── requirements.txt   # Simulator/benchmark dependencies beyond `rlinf`
├── configs/           # Training or evaluation Hydra YAML configs
└── <module>/          # Environment wrapper, action formatting, and custom EnvWorker / entry script
```

## Integration Note

`SupportedEnvType` and `get_env_cls()` in `rlinf/envs/__init__.py` do not yet provide a dynamic `register_env()` hook for `RLINF_EXT_MODULE`. To integrate a simulator out of tree without modifying core RLinf, provide a custom `EnvWorker` subclass or launch script inside your `envs/<env_name>/` folder (and use `RLINF_EXT_MODULE` for any companion models or algorithms).

See the [New Environment Guide](https://rlinf.readthedocs.io/en/latest/rst_source/extending/new_env.html) for RLinf's environment contract.
