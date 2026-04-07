# To study series resonance curve
import numpy as np
import matplotlib.pyplot as plt
def lcr_current(f, E,R, C, L):
    w = 2 * np.pi * f # angular frequency 
    Z = R + 1j * (w * L - 1 / (w * C)) # impedance
    I = E / Z # current I_max
    return I
f = np.linspace(50, 5000, 1000)
I = lcr_current(f,E=5,R=100,C=0.1e-6,L=100e-3) 
plt.plot(f, abs(I))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Current (A)')
plt.title('Series Resonance Curve')
plt.show()