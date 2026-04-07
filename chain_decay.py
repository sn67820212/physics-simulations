# Radioactive chain decay
import numpy as np
import matplotlib.pyplot as plt

#variable declaration
n_Bi_213 = 10000 #number of Bi-213 atoms
tau_Bi_213 = 46 * 60 #half life of Bi-213
n_Tl = 0 #number of Tl-209 atoms
tau_Tl = 2.2 * 60 #half life of Tl-209
n_Pb = 0 #number of Pb-209 atoms
tau_Pb = 3.3 * 60 #half life of Pb-209
n_Bi_209 = 0 #number of Bi-209 atoms
t_max = 10000

#list declaration
t_points = np.linspace(0,t_max,10000)
n_Bi_213_points = []
n_Tl_points = []
n_Pb_points = []
n_Bi_209_points = []

#to assign decay probability for each atom
p_Bi = 1 - 2 ** (-1/tau_Bi_213)
p_Tl = 1 - 2 ** (-1/tau_Tl)
p_Pb = 1 - 2 ** (-1/tau_Pb)

#monte carlo simulation
for j in t_points:
    n_Bi_213_points.append(n_Bi_213)
    n_Tl_points.append(n_Tl)
    n_Pb_points.append(n_Pb)
    n_Bi_209_points.append(n_Bi_209)
    for i in range(n_Pb):
        if np.random.rand() < p_Pb:
            n_Pb -= 1
            n_Bi_209 += 1
    for i in range(n_Tl):
        if np.random.rand() < p_Tl:
            n_Tl -= 1
            n_Pb += 1
    for i in range(n_Bi_213):
        if np.random.rand() < p_Bi:
            n_Bi_213 -= 1
            if np.random.rand() < 0.9791:
                n_Pb += 1
            else:
                n_Tl += 1

#plotting
plt.plot(t_points, n_Bi_213_points, label = 'Bi-213')
plt.plot(t_points, n_Tl_points, label = 'Tl-209')
plt.plot(t_points, n_Pb_points, label = 'Pb-209')
plt.plot(t_points, n_Bi_209_points, label = 'Bi-209')        
plt.xlabel('Time (s)')
plt.ylabel('Number of atoms')
plt.title('Radioactive chain decay')
plt.legend()
plt.show()