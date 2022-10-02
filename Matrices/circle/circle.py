import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
#sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts

#local imports
#from line.funcs import *
#Efrom triangle.funcs import *
#from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
#Input parameters
a = 8
c = 3
d = 4
r = 5 #radius
theta1 = 2*mp.atan(r/d) #ang ADC
theta2 = 2*mp.atan(r/a) #ang BAD
theta3 = 2*mp.atan(r/c) #ang BCD
print(theta1,theta2,theta3)
D = np.array(([0,0]))
O = np.array(([d,r])) # centre
e1 = np.array(([1,0]))
C = (c+d)*e1
A = (a+d)*np.array(([mp.cos(theta1),mp.sin(theta1)]),dtype='float64')


#Generating the director vectors

m1 = np.array(([1 ,mp.tan(theta1+theta2)]),dtype='float64')
m2 = np.array(([1 ,-mp.tan(theta3)]),dtype='float64')

matM = np.block([[m1],[m2]]).T
lam = LA.solve(matM,C-A)
B = A + lam[0]*m1
#B = C - lam[1]*m2

#print(B)

##Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(C,B)
x_AD = line_gen(A,D)
x_DC = line_gen(D,C)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])#,label='$Diameter$')
plt.plot(x_BC[0,:],x_BC[1,:])#,label='$Diameter$')
plt.plot(x_AD[0,:],x_AD[1,:])#,label='$Diameter$')
plt.plot(x_DC[0,:],x_DC[1,:])#,label='$Diameter$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')


#Labeling the coordinates
tri_coords = np.vstack((A,C,D,B,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','C','D','B','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
print("figure generated")
plt.savefig('/sdcard/Download/Matrices/circle/circle.png')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-14.pdf"))
#else
#plt.show()
