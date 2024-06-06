import gym
import gym_minigrid

# 创建MiniGrid环境
env = gym.make('CartPole-v0')

# 重置环境并获取初始观察
obs = env.reset()

# 执行循环来模拟小车在环境中移动
i = 0
done = False
while not done:
    # 渲染环境（可选）
    env.render()



    # 随机选择一个动作
    # action = env.action_space.sample()

    # 第一个简单的策略，以后我们在这里扩充！！！
    action = 2
    if i == 14:
        action = 1

    i = i + 1
    # 执行动作并获取下一个状态、奖励和终止标志
    obs, reward, done, info, _ = env.step(action)

# 关闭环境
env.close()
