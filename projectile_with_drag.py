#projectile with drag
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#parameters
g = 9.8
k = 0.3
v0 = 45
theta = 45/180*np.pi

#initial conditions: [vx0,vy0]
vx0 = v0*np.cos(theta)
vy0 = v0*np.sin(theta)
y0 = [vx0,vy0]

#ode function
def projectile(t,y):
    vx,vy = y
    dvx_dt = -k*vx
    dvy_dt = -g - k*vy
    return [dvx_dt,dvy_dt]

#solve from t = 0 to 5
t_span = (0,5)
t_eval = np.linspace(0,5,1000)
sol = solve_ivp(projectile,t_span,y0,t_eval=t_eval)

#extract solutions
t = sol.t
vx = sol.y[0]
vy = sol.y[1]

#positions
x = np.cumsum(vx)*(t[1]-t[0])
y = np.cumsum(vy)*(t[1]-t[0])

#plot
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()