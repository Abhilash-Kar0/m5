from gym import Env
from gym.envs.registration import register
from gym.utils import seeding
from gym import spaces
import numpy as np

import sys
import os
import time
import copy

class gridworld(Env):
    

    def __init__(self,Variant):
        self.actions = [0,1,2,3]
        self.action_space = spaces.Discrete(4)
        self.action_mapping = {0:[-1, 0], 1:[1,0], 2:[0,-1], 3:[0,1]}
        
        self.ob_shape = (12,12)
        self.observation_space = spaces.Box(low=1,high=12,shape = self.ob_shape,dtype = np.int)

        self.Variant = Variant

        self.all_start_states = [(6,1),(7,1),(11,1),(12,1)]
        self.agent_start_state = self.all_start_states[np.random.choice(np.asarray(range(4)))]
        self.agent_goal_state = None

        if self.Variant == 'A':
            self.agent_goal_state = (1,12)
        elif self.Variant == 'B':
            self.agent_goal_state = (3,10)
        elif self.Variant == 'C':
            self.agent_goal_state = (7,8)
        else:
            print("error")
            exit()
        
        self.current_state = copy.deepcopy(self.agent_start_state)

        self.puddle1 = [(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(3,5),(9,5),(3,6),(9,6),(3,7),(9,7),(3,8),(7,8),(8,8),(9,8),(3,9),(4,9),(5,9),(6,9),(7,9)]
        self.puddle2 = [(4,5),(5,5),(6,5),(7,5),(8,5),(4,6),(8,6),(4,7),(6,7),(7,7),(8,7),(4,8),(5,8),(6,8)]
        self.puddle3 = [(5,6),(6,6),(7,6),(5,7)]

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        reward = 0
        if np.random.random()<0.1:
            act_set = self.actions.copy()
            act_set.remove(action)
            action = np.random.choice(act_set)

         
        next_state = [self.current_state[0]+self.action_mapping[action][0],self.current_state[1]+self.action_mapping[action][1]]

        if np.random.random()<0.5 and self.Variant != 'C':
            next_state[1]+=1
            next_state[1]=min(next_state[1],12)
        
        if next_state[0]<=0 or next_state[0]>self.ob_shape[0] or next_state[1]<=0 or next_state[1]>self.ob_shape[1]:
            next_state = self.current_state
        
        next_state = tuple(next_state)

        if next_state in self.puddle1 :
            reward = -1
        elif next_state in self.puddle2 :
            reward = -2
        elif next_state in self.puddle3 :
            reward = -3
        if next_state == self.agent_goal_state:
            reward += 10
            return next_state,reward,True,{}
        

        self.current_state = next_state
        return next_state,reward,False,{} # Return the next state and the reward, along with 2 additional quantities : False, {}
 

    def reset(self):
        self.agent_start_state = self.all_start_states[np.random.choice(np.asarray(range(4)))]
        self.current_state = copy.deepcopy(self.agent_start_state)
        return self.current_state

    def render(self):
        pass



        

        


        