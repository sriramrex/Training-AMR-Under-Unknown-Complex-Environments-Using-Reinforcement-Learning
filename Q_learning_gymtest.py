import glob
import io
import base64

import gym
import my_gym3
import numpy as np
import datetime
import torch


from torch.utils.tensorboard import SummaryWriter
now = datetime.datetime.now()
writer = SummaryWriter(log_dir = '../tensorboard_session/q_learning_stage1_' + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute))


def init_q(s, a, type="ones"):
    """
    @param s the number of states
    @param a the number of actions
    @param type random, ones or zeros for the initialization
    """
    if type == "ones":
        return np.ones((s, a))
    elif type == "random":
        return np.random.random((s, a))
    elif type == "zeros":
        return np.zeros((s, a))

def epsilon_greedy(Q, epsilon, n_actions, s, train=False):
    """
    @param Q Q values state x action -> value
    @param epsilon for exploration
    @param s number of states
    @param train if true then no random actions selected
    """
    
    if train or np.random.rand() < epsilon:
        action = np.argmax(Q[s, :])
        
    else:
        action = np.random.randint(0, n_actions)
    return action

def test_agent(Q, env, n_tests, n_actions, delay=0.5):
    
    for test in range(n_tests):
        print(f"Test #{test}")
        s = env.reset()[0]
        done = False
        epsilon = 0
        total_reward = 0
        while True:
            time.sleep(delay)
            a = epsilon_greedy(Q, epsilon, n_actions, s, train=True)
            print(f"Chose action {a} for state {s}")
            s, reward, terminated, truncated, info = env.step(a)
            done = truncated or terminated
            total_reward += reward
            print ("State", s)
            if done:
              print(f"Episode reward: {total_reward}")
              if s == 47:
                  print("Reached goal!")
              else:
                  print("Shit! dead x_x")
              time.sleep(3)
              break

def qlearning(env, alpha, gamma, epsilon, episodes, max_steps, n_tests, render=False, test=False):
    """
    @param alpha learning rate
    @param gamma decay factor
    @param epsilon for exploration
    @param max_steps for max step in each episode
    @param n_tests number of test episodes
    """
    n_states = env.observation_space.shape[0]
    n_actions = env.action_space.n
    
    Q = init_q(n_states, n_actions, type="ones")
    print(Q)
    timestep_reward = []
    epsilon_decay = 0.00001
    for episode in range(episodes):        
        s = env.reset()[0]       
        t = 0
        total_reward = 0
        done = False
        
        while t < max_steps:
            t += 1
            
            a = epsilon_greedy(Q, epsilon, n_actions, s)

            s_, reward, terminated, truncated, info = env.step(a)
            done = truncated or terminated
            total_reward += reward                       
            a_ = np.argmax(Q[s_, :])
            if done:
                Q[s, a] += alpha * (reward  - Q[s, a])
            else:
                Q[s, a] += alpha * (reward + (gamma * Q[s_, a_]) - Q[s, a])
            s = s_
            if epsilon > 0.05:
              epsilon -= epsilon_decay
            if done:
                timestep_reward.append(total_reward)
                break

    if test:
        test_agent(Q, env, n_tests, n_actions)
    return timestep_reward

if __name__ =="__main__":
  env_name = "turtlebot_stage1_dis-v0"
  env = gym.make(env_name)
  alpha = 0.1
  gamma = 0.9
  epsilon = 0.99
  episodes = 1000
  max_steps = 2500
  n_tests = 2
  timestep_reward = qlearning(env, alpha, gamma, epsilon, episodes, max_steps, n_tests, test=True)
  print(timestep_reward)

writer.add_scalar('Train/Reward', timestep_reward, episodes)

