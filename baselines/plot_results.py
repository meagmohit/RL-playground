from baselines.common import plot_util as pu
import matplotlib.pyplot as plt
import numpy as np

# Parameters
dir_name = 'openai-2018-11-06-21-19-32-539241'
game_name = 'Pong'

results = pu.load_results(dir_name)
r = results[0]

plt.plot(np.cumsum(r.monitor.l), pu.smooth(r.monitor.r, radius=10))
plt.title(game_name)
plt.xlabel('# of timesteps')
plt.ylabel('Reward')
#plt.show()
plt.savefig(game_name+'_rewards.png', bbox_inches='tight')
