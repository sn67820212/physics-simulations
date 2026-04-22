# integration by mean value method using Monte Carlo Simulation
import numpy as np
#step 1: Define function to be integrated
def f(x):
    return (np.sin(1/(x*(2-x))))**2
#step 2: Define the integration interval
a = 0
b = 2
#step 3: Define the number of sample points
N = 10000
count = 0
#step 4: use hit and miss method
for i in range(N):
    x = np.random.rand()
    y = 2*np.random.rand()
    if y <= f(x):#hits the region below the curve
        count += 1
I = (b-a)*2*count/N
print("the value of integral is",I)