import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

samples=70
x = np.linspace(-1,3,samples)
randvar = np.loadtxt('./uni1.dat',dtype='double') + np.loadtxt('./uni2.dat',dtype='double')
cdf1 = []
for i in range(0,samples):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	cdf1.append(err_n/int(1e6)) #storing the probability values in a list
	
pdf1 = np.gradient(cdf1, x, edge_order=2)
pdf = np.piecewise(x,[((x<0)&(x>=2)),((x>=0)& (x<1)), ((x>=1)&(x<2))],[0,lambda x:x,lambda x:(2-x)])
cdf =np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x**2/2, lambda x: 2*x - x**2/2 - 1, 1]) 
plt.plot(x,pdf1)
plt.plot(x,pdf,'o')
plt.legend(['Formulated PDF','Theoretical PDF'])
plt.savefig('../figs/sumofrv_pdf.pdf')
plt.savefig('../figs/sumofrv_pdf.png')
plt.show()
plt.close()
plt.plot(x,cdf1)
plt.plot(x,cdf,'o')
plt.legend(['Formulated CDF','Theoretical CDF'])
plt.savefig('../figs/sumofrv_cdf.pdf')
plt.savefig('../figs/sumofrv_cdf.png')

plt.show()
