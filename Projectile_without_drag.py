"""projectile motion curve in vaccum"""
import numpy as np,matplotlib.pyplot as plt
g = 9.8
def curve(u,q):#u is initial velocity and q is angle 
    # time period
    t = 2*u*np.sin(q)/g
    t_steps = np.linspace(0,t,1000)
    x = u*t_steps*np.cos(q)
    y = u*t_steps*np.sin(q)-0.5*g*t_steps**2
    return x,y
plt.plot(curve(100,40/180*np.pi)[0],curve(100,40/180*np.pi)[1])
plt.plot(curve(100,50/180*np.pi)[0],curve(100,50/180*np.pi)[1])
plt.show()
#the code shows that two points correspond to two different parabolas 
# In detail, consider two points, join them by a line.. consider parabolas that have these points but the \n
#tangent at minima  is parallel to lne joining these two points, interestingly, u get 2 parabolas
#this doesn't show that there can be more than 2 parabolas but it shows at least 2 exist of such nature