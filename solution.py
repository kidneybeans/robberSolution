# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:17:13 2018

@author: kidneybeans
"""
import numpy as np

n = 7
cost = [30, 50, 10, 30, 20, 100, 20]

class solution(object):
     def __init__(self, n, cost):
         self.num = n
         self.cost = cost
         self.dp = np.zeros(self.num, dtype = np.int16)
         self.prev = np.zeros(self.num, dtype = np.int16)
     
     def solve(self):
         self.dp[0] = self.cost[0]
         self.prev[0] = 0
         self.dp[1] = max(self.cost[0], self.cost[1])
         self.prev[1] = 1 if self.dp[1] == self.cost[1] else 0

         for i in range(2, self.num):
             self.dp[i] = max(self.dp[i-1], self.dp[i-2] + self.cost[i])
             self.prev[i] = i-1 if self.dp[i] == self.dp[i-1] else i-2
             
         for i in range(self.num)[::-1]:
             print("[current] %d, [dp] %d, [prev]: %d"%(i, self.dp[i],self.prev[i]))
        
         print('+++++++++++++++++++++++++++++++++++++++')
         
         last = 0
         for i in range(self.num)[::-1]:
             if i == self.num-1:
                 print("[current] %d, [next] %d"%(i, self.prev[i]))   
             else:
                 if i == last:
                     print("[current] %d, [next] %d"%(i, self.prev[i]))            
             last = self.prev[i]
              
testSolution = solution(n, cost)
testSolution.solve()

            
