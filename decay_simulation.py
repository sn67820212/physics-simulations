"""Radioactive decay simulation using Monte Carlo method.
Models Thallium nucleus decay over time with visualization.
"""
import random as rd
import numpy as np
import matplotlib.pyplot as plt
def decay(n_tl,tau,t_max,n_pb=0):
    # n_tl,n_pb indicate number of Tl and Pn atoms
    #tau represents half lifetime of parent nuclei
    #t_max is total time 
    t_points = np.linspace(0,t_max,1000)
   p = 1 - 2 ** (-1/tau)  # Decay probability per timestep from exponential decay law
    n_tl_points = []
    n_pb_points = []
    for j in t_points:
        n_tl_points.append(n_tl)
        n_pb_points.append(n_pb)
        decayed = 0
        for i in range(n_tl):
            if rd.random() < p:
                decayed += 1
        n_tl -= decayed
        n_pb += decayed
    return t_points,n_tl_points,n_pb_points
problem = decay (1000,3.053*60,1000)
plt.plot(problem[0], problem[1], label='Parent (Tl-201)')
plt.plot(problem[0], problem[2], label='Daughter (Pb)')
plt.xlabel('Time (s)')
plt.ylabel('Number of Atoms')
plt.legend()
plt.show()
