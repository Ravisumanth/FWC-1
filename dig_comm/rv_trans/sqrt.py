import numpy as np
import matplotlib.pyplot as plt


cdf=[]
samples = 100
simlen = int(1e6)
x = np.linspace(0,10,samples)
x1 = np.random.normal(0,1,simlen)
x2 = np.random.normal(0,1,simlen)
A = np.sqrt(x1**2+x2**2)
for i in range(samples):
    arr = np.nonzero(A<x[i])
    count = np.size(arr)
    cdf.append(count/simlen)

pdf = np.gradient(cdf, x,edge_order=2)


#finding the above functions theoretically
def theo_cdf(a):
    return 1-np.exp(-a**2/2)
def theo_pdf(a):
    return a*np.exp(-a**2/2)


plt.plot(x,pdf)
plt.plot(x,theo_pdf(x),'o')
plt.savefig("../figs/square_root_pdf.pdf")
plt.legend(['formulated','theoretical'])
plt.show()
plt.close()
plt.plot(x,cdf)
plt.plot(x,theo_cdf(x),'o')
plt.legend(['formulated','theoretical'])
plt.savefig("../figs/square_root_cdf.pdf")
plt.show()
