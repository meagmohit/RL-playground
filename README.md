# RL-playground
Important codes for learning and testing SOTA RL algorithms


## Rainbow
-----------
Forked from [https://github.com/Kaixhin/Rainbow](https://github.com/Kaixhin/Rainbow)
  * Works on python 2.7 and pytorch 0.4


## OpenAI Baselines
--------------------
Forked from [https://github.com/openai/baselines](https://github.com/openai/baselines)
  * Works on python 2.7 and tensorflow-gpu
  * Run as `OPENAI_LOGDIR=<PATH for logs> python -m baselines.run --alg=deepq --env=SpaceInvadersNoFrameskip-v4 --num_timesteps=1e7 --save_path=<path_to_model>`
  * OR set `export OPENAI_LOGDIR=<PATH>` and `export OPENAI_LOG_FORMAT=stdout,csv,log,tensorboard`
  * For plotting, provide the path of log directory relative to the location of `plot_results.py`
  * Plotting doesn't work on Python 2.7 environment

## References
--------------------
