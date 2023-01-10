import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy.stats


maxrange=100
maxlim=5
x = np.linspace(-maxlim,maxlim,maxrange)    #points on the x axis
simlen = int(1e6) #number of samples
prob = [] #declaring probability list
pdf = [] #declaring pdf list
randvar = np.loadtxt("gau.dat", dtype='double')


#for i in range(0,maxrange):
#	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
#	err_n = np.size(err_ind) #computing the probability
#	prob.append(err_n/simlen) #storing the probability values in a list

#find cdf values in this way too!
prob = scipy.stats.norm.cdf(x)

#pdf here is generated from cdf
pdf = np.gradient(prob, x, edge_order=2)


#probability distribution function mathematically
def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)
#vec_gauss_pdf = scipy.vectorize(gauss_pdf)

#print(len(prob),len(x))
plt.plot(x,prob)  #plotting the CDF
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.savefig('../figs/gauss_cdf.pdf')
plt.savefig('../figs/gauss_cdf.png')
plt.show()
plt.close()


#plotting pdf
plt.plot(x,pdf,'o')             # plotting PDF derived from CDF
plt.plot(x,gauss_pdf(x))    # plotting mathematical PDF
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["FOrmulated PDF","Theoretical PDF"])
plt.savefig('../figs/gauss_pdf.pdf')
plt.savefig('../figs/gauss_pdf.png')
plt.show()
plt.savefig('../figs/gauss_pdf.pdf')
