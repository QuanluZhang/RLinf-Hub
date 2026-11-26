# Models

Community embodied and agentic model integrations built on [RLinf](https://github.com/RLinf/RLinf) (VLA policies, World Action Models, world model backends, multimodal/reasoning LLMs and VLMs, and reward/value models).

See open model tasks in [RLinf/RLinf#1943](https://github.com/RLinf/RLinf/issues/1943).

## Directory Layout

Place each model in its own subfolder:

```text
models/<model_name>/
├── README.md          # Paper/checkpoint links, setup, launch command, tested RLinf version, and results
├── README.zh-CN.md    # Chinese README
├── requirements.txt   # Model-specific dependencies beyond `rlinf`
├── configs/           # SFT, RL, or evaluation Hydra YAML configs
└── <module>/          # Model builder and policy wrapper registered via RLINF_EXT_MODULE
```

## Registration Hooks

Register your model from your `RLINF_EXT_MODULE` entry point using `register_model(model_type, builder, category=...)` in `rlinf.models` and `SupportedModel.register(...)` in `rlinf.config` (see the [New Model Guide](https://rlinf.readthedocs.io/en/latest/rst_source/extending/new_model_fsdp.html)).

If your integration requires changes in core [RLinf/RLinf](https://github.com/RLinf/RLinf) (such as a new extension hook or interface update), open an issue in [RLinf/RLinf](https://github.com/RLinf/RLinf/issues) or [RLinf/RLinf-Hub](https://github.com/RLinf/RLinf-Hub/issues) to let us know.
