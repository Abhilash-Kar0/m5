from gym.envs.registration import register

register(
    id='Gridworld-q1-v0',
    entry_point='gridworld_env.gridworld_env:gridworld',
)