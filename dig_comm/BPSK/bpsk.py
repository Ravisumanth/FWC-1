import numpy as np
import matplotlib.pyplot as plt

lensamp = 1000
X = np.random.binomial(1,0.5,lensamp)
N = np.random.normal(0,1,lensamp)
A_db = 3
A = 10**(A_db*0.1)
Y = A*X+N

plt.plot(Y,np.zeros(1000), 'o')
#plt.xlabel(


plt.show()
