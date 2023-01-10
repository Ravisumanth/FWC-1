import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


uni_data = np.loadtxt("uni.dat")
V = -2*np.log(1-uni_data)
x = np.linspace(0,20,50)
#V_cdf = scipy.stats.norm.cdf(V[:100])
x2= np.sort(V)
y2 = np.array(range(int(1e6)))/float(1e6)

#finding the cdf mathematically
def cdf_math(x):
    return np.piecewise(x,[x<0,x>=0],[0,lambda x: 1-np.exp(-x/2)])
plt.plot(x2,y2)
plt.plot(x,cdf_math(x),'o')
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Formulated CDF","Theoretical CDF"])
plt.savefig('../figs/log_func_cdf.pdf')
plt.savefig('../figs/log_func_cdf.png')
plt.show()
