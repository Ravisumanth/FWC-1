import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import subprocess
import shlex
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def rhmbs_vertices(d1,d2):
    A = np.array([d1/2,0])
    B = np.array([0,d2/2])
    C = np.array([-d1/2,0])
    D = np.array([0,-d2/2])
    return A,B,C,D


def line_gen(A,B):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i] = temp1.T
    return x_AB

#Rhombus can be constructed using two diagonal lengths;
d1 = 8
d2 = 6
[A,B,C,D] = rhmbs_vertices(d1,d2)
#line generation
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)
x_AC = line_gen(A,C)
x_BD = line_gen(B,D)

plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')


rhm_vert = np.vstack((A,B,C,D)).T
plt.scatter(rhm_vert[0,:],rhm_vert[1,:])
vert_labels = ['A','B','C','D']

for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
            (rhm_vert[0,i], rhm_vert[1,i]),
            textcoords = 'offset points',
            xytext = (0,10),
            ha='center')


plt.xlabel('$x$')                    
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('/sdcard/Download/Matrices/line/rhombus.png')














