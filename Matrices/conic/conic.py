import numpy as np
import matplotlib.pyplot as plt
r = 5
coeff = [1,-4,-12]
A = np.roots(coeff)
print(A)
x = np.linspace(0,12,50)
y = np.linspace(-6,6,50)
a,b = np.meshgrid(x,y)
c = (a-A[0])**2+b**2-(r**2)
#c1 = (a-A[1])**2+b**2-(r**2)
figure,axes = plt.subplots()
axes.contour(a,b,c,[0])
#axes.contour(a,b,c1,[0])------Circle with radius(-2,0)
axes.set_aspect('equal')
#plt.show()
plt.savefig('/root/ravi/FWC-1/Matrices/conic/conic.png')
