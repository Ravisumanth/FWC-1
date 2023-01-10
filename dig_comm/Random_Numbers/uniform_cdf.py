import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


samples = 30      #on x-axis
#x = np.linspace(-4,4,samples)
x = np.arange(-4,4,0.2666666667)#points on the x axis
simlen = int(1e6) #number of samples
prob = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#print(randvar)


#below gives the cdf. it can also be generated using histogram or sort() method
#for i in range(0,samples):
	#err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	#err_n = np.size(err_ind) #computing the probability
	#prob.append(err_n/simlen) #storing the probability values in a list
prob = scipy.stats.uniform.cdf(x)


plt.plot(x,prob)#plotting the CDF
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.savefig('../figs/uniform_cdf.png')
plt.savefig('../figs/uniform_cdf.pdf')

plt.show() #opening the plot window
