# Algorithms

Community RL and post-training algorithm implementations and paper reproductions built on [RLinf](https://github.com/RLinf/RLinf) (flow/diffusion RL, offline-to-online VLA RL, humanoid control RL, and agentic RL).

See open algorithm tasks in [RLinf/RLinf#1943](https://github.com/RLinf/RLinf/issues/1943).

## Directory Layout

Place each algorithm in its own subfolder:

```text
algorithms/<algorithm_name>/
├── README.md          # Paper link, setup, launch command, tested RLinf version, and curves/logs
├── README.zh-CN.md    # Chinese README
├── requirements.txt   # Extra dependencies beyond `rlinf` (if any)
├── configs/           # Hydra YAML configs
└── <module>/          # Advantage/loss/worker code registered via RLINF_EXT_MODULE
```

## Registration Hooks

Use RLinf's registries from your `RLINF_EXT_MODULE` entry point:
- `@register_advantage("<name>")` in `rlinf.algorithms.registry`
- `@register_policy_loss("<name>")` in `rlinf.algorithms.registry`
- `register_reward("<name>", cls)` in `rlinf.algorithms.rewards`

If your integration requires changes in core [RLinf/RLinf](https://github.com/RLinf/RLinf) (such as a new extension hook or interface update), open an issue in [RLinf/RLinf](https://github.com/RLinf/RLinf/issues) or [RLinf/RLinf-Hub](https://github.com/RLinf/RLinf-Hub/issues) to let us know.
