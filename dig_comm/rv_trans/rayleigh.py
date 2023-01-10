import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()

min_gamma = 0
max_gamma = 10
ray_prob = []
ray_theo = []
gamma_db = np.arange(min_gamma,max_gamma)
simlen = int(1e6)
N = np.random.normal(0,1,simlen)
for i in gamma_db:
    gamma = 10**(0.1*i)
    A = rng.rayleigh(np.sqrt(gamma/2),simlen)
    ray_prob.append(np.count_nonzero(A+N<0)/simlen)
    ray_theo.append(0.5-0.5*np.sqrt(gamma)/np.sqrt(2+gamma)) #theoretical method

plt.semilogy(gamma_db,ray_prob,'o')
plt.semilogy(gamma_db,ray_theo)
plt.xlabel('gamma')
plt.ylabel('$P_X(X_est=1)|(X=1)$')
plt.legend(['formulated','theoretical'])
plt.savefig('../figs/rayleigh.pdf')
plt.show()
