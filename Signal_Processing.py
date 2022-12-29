#Code by Ravi Sumanth Muppana, work in progress
#This file consists of exercises on digital communication and signal processing
#based on Dr. GVV Sharma's ongoing work on Signal Processing, IIT-H


import numpy as np
import sympy
from sympy.plotting import plot
from sympy.abc import t,s,a
from sympy import symbols
from sympy import plot_implicit, symbols, Eq, And
import matplotlib.pyplot as plt

x,y = np.roots([1,-1,1])
#print(x,y)

def a_n(i):
    while(i>=1):
        return ((x**i-y**i)/(x-y))

def b_n(i):
    if(i==1):
        return 1
    while(i>=2):
        q1 = a_n(i-1)
        q2 = a_n(i+1)
        return q1+q2
#example to find b_n() function, uncomment and run the code
#print(b_n(2))


#pingala series problem
def x_n(i):
    if(i==1 or i==0):
            return 1
    while(i>=0):
            return int(x_n(i-2)+x_n(i-1))
    return int(x_n(i+2)-x_n(i+1))


#function to print pingala seq and plot a stem
def plot_stem(k):
    y=[]
    x=range(k)
    for i in range(k):
        y.append(x_n(i))
    plt.stem(y,x)
    #return plt.show()
#example is below, uncomment and run the code
# plot_stem(15)


def y_n(i):
    while(i>=0):
        return x_n(i-1)+x_n(i+1)
y=[]
k = 5
for i in range(k):
    y.append(y_n(i))
x = range(k)
#print(y)
#plt.stem(y,x,linefmt='red')
#plt.show()

#circuits and transforms using latex-tikz
#laplace transform
def laplace_trans(f):
    return sympy.laplace_transform(f,t,s)
#print(laplace_trans(sympy.exp(-a*t)*sympy.Heaviside(t)))
#In sympy, unit step function u(t) is termed as Heaviside(t), although at t=0 one point, it results in 0.5


#filters
#applying a digital filter to reduce noise in a wav file
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf

order=2
cut_off = 5100 #Hz
input_sig, fs = sf.read('Sound_Noise.wav')
dig_freq = 2*(cut_off/fs)
#b,a are polynomials for computing
b,a = signal.butter(order,dig_freq,'low',output='ba')
#filtfilt filters twice, forward and backward to have zero phase shift
output = signal.filtfilt(b,a,input_sig)
#can use lfilter() too
# print(output)
#sf.write('filtered_sig2.wav',output,fs)

#solving difference equation
xn = ([1,2,3,4,2,1])
#plt.stem(xn)
k= 20
yn = np.zeros(k)
def y_out(i):
    if i<0:
        return 0
    elif i<2:
        return -0.5*y_out(i-1)+xn[i]
    elif i<6:
        return -0.5*y_out(i-1)+xn[i]+xn[i-2]
    elif i>5 and i<8:
        return -0.5*y_out(i-1)+xn[i-2]
    elif i>7:
        return -0.5*y_out(i-1)
    
val=[]
for i in range(15):
    val.append(y_out(i))
#plt.stem(val)
#plt.show()

#Impulse response of a filter
n,z = sympy.symbols('n z')
def hn(n):
    return ((-0.5)**n)*sympy.Heaviside(n,1)+((-0.5)**(n-2))*sympy.Heaviside(n-2,1) 
arr = []
for i in range(12):
    arr.append(hn(i))
#plt.stem(arr)
#plt.show()

#plotting of discrete time fourier transform function to above y_out(n)
def dtft(z):
    num = np.polyval([1,0,1],z**(-1))
    den = np.polyval([0.5,1],z**(-1))
    return num/den
omega = np.linspace(-3*np.pi,3*np.pi,200)
#plt.plot(omega,abs(dtft(np.exp(1j*omega))))
#plt.show()
H = dtft(z)

#determining stability of a continuous systems using laplace functions
import control
num = np.array([2,2])
den = np.array([2,1,0])
H = control.tf(num,den)
print(H)
p = control.pole(H)
print(p)
t,y = control.step_response(H)
plt.grid()
control.pzmap(H)
plt.show()