#Code by Amey Waghmare, 
#Jan 16, 2020
#Revised by GVV Sharma
#Jan 17, 2020
#Released under GNU GPL
#Quadratic program example
#using cvx
import numpy as np
from cvxpy import *


#Problem parameters
P = np.array([2,3,4]).reshape(3,-1)
n = np.array([2,1,3]).reshape(3,-1)
c = np.array([26]).reshape(1,1)

x = Variable((3,1))

#Cost function
f =  quad_form(x-P, np.eye(3))
obj = Minimize(f)

#Constraints
constraints = [n.T@x == c]

#solution
Problem(obj, constraints).solve()

print(np.sqrt(f.value),x.value)
