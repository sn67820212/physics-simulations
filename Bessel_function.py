'''Write a Python function J(m,x) that calculates the value of J_m(x) using Simpson'srule with N
1000 points. Use your function in a program to make a plot, on a single graph, of the Bessel
functions J_o, J_1, and J_2 as a function of x from x = 0 to 20.'''
import numpy as np
import matplotlib.pyplot as plt
def bessel_function(n, x):
    a = 0
    b = np.pi
    N = 1000
    h = (b - a) /N
    k = int(N/2)
    def f(t):
        return np.cos(n*t - x*np.sin(t))
    s = f(a) + f(b)
    for i in range(1, k+1):
        s += 4*f(a + (2*i - 1)*h)
    for i in range(1,k+1):
        s += 4*f(a + 2*i*h)
    return h*s/3
x = np.linspace(0, 20,1000)
J0 = [bessel_function(0, xi) for xi in x]
J1 = [bessel_function(1, xi) for xi in x]
J2 = [bessel_function(2, xi) for xi in x]
plt.plot(x, J0, label='J0')
plt.plot(x, J1, label='J1')
plt.plot(x, J2, label='J2')
plt.xlabel('x')
plt.ylabel('J_n(x)')
plt.title('Bessel Functions J0, J1, J2')
plt.legend()
plt.grid()
plt.show()