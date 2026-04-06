import random as rd
import numpy as np
import matplotlib.pyplot as plt
def decay(n_tl,tau,t_max,n_pb=0):
    t_points = np.linspace(0,t_max,1000)
    p = 1 - 2 ** (-1/tau) #p is the probability of decay
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
plt.plot(problem[0],problem[1])
plt.plot(problem[0],problem[2])
plt.show()