import numpy as np
#import mpmath as mp
import math
import matplotlib.pyplot as plt
from numpy import linalg as LA
#from coeffs import *
import sys                                             #for path to external scripts
sys.path.insert(0,'/sdcard/Download/CoordGeo')

from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if
#if using termux
import subprocess
import shlex
#end if

O = np.array(([0,0]))
Z1 = 2
Z2=3
e1=np.array(([1,0]))
e2=np.array(([0,1]))
A=Z1*e1
B=Z2*e2
C=-Z1*e1
D=-Z2*e2
if (((A+C)//2 == (B+D)//2).all() and (np.dot((A-C),(B-D).T)==0).all()):
    print('Diagonals bisect each other at` right angles')
else:
    print('False')
#Generating all lines

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)
x_AC = line_gen(A,C)
x_BD = line_gen(B,D)

plt.plot(x_AB[0,:],x_AB[1,:],color='g')
plt.plot(x_BC[0,:],x_BC[1,:],color='g')
plt.plot(x_CD[0,:],x_CD[1,:],color='g')
plt.plot(x_DA[0,:],x_DA[1,:],color='g')
plt.plot(x_AC[0,:],x_AC[1,:],color='r')
plt.plot(x_BD[0,:],x_BD[1,:],color='r')

#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()

plt.savefig('/sdcard/Download/Matrices/line/rhombus.png')
#subprocess.run(shlex.split("termux-open /sdcard/Download/Line/fig/fig5.pdf"))
#plt.show()
#
#
#
#
