import numpy as np
import matplotlib.pyplot as plt

#Define the parameters
L = 101 #length of the box
x_list = []
y_list = []
dxdy = [(-1,0),(1,0),(0,-1),(0,1)] #left,right, up, down

#Define the random walk
def random_walk(n):#n is the number of steps
    x = y = 50 # Initial position
    for i in range(n):
        x_list.append(x)
        y_list.append(y)
        step = dxdy[np.random.randint(0,4)]
        #Check if the particle is out of the box
        if x+step[0] < 0 or x+step[0] > L-1 or y+step[1] < 0 or y+step[1] > L-1:
            # bounce back from walls
            x = x - step[0] 
            y = y - step[1]           
        else:
            x = x + step[0]
            y = y + step[1]
    return x_list, y_list

#Simulation of 1000 steps
x_list, y_list = random_walk(100000)

#density plot
plt.hist2d(x_list,y_list)
plt.colorbar(label = 'no. of visits')
plt.show()