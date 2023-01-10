import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


samples= int(1e6)
X2 = np.random.normal(0,1,samples)
X1 = np.random.normal(0,1, samples)
V = X1**2+X2**2
cdf = []
x = np.arange(0,10,1)
for i in range(0,10):
    arr = np.nonzero(V<x[i])
    count = np.size(arr)
    cdf.append(count/samples)
pdf = np.gradient(cdf,2)
plt.plot(x,pdf)
plt.xlabel("x")
plt.ylabel("$f_X(x)$")
plt.savefig("../figs/sos_pdf.pdf")
plt.show()
plt.close()
plt.plot(x,cdf)
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.savefig("../figs/sos_cdf.pdf")
plt.show()
