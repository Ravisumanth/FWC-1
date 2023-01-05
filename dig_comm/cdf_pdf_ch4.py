import numpy as np
import matplotlib.pyplot as plt

samples= int(1e6)
X2 = np.random.normal(0,1,samples)
X1 = np.random.normal(0,1, samples)
V = X1**2+X2**2
x = np.linspace(-2,2,100)
count,bins = np.histogram(V,x)
pdf = count/samples
cdf = np.cumsum(pdf)
#plt.plot(count)
plt.plot(bins[0:99],cdf)
plt.show()
