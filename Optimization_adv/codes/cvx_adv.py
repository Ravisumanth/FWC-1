import cvxpy as cp
import numpy as np
from numpy import linalg as LA

X = cp.Variable(shape=(3,1),name='X')
P = np.array([[2],[3],[4]])
O = np.array([[2],[1],[3]])
constraints = [O.T@X==26]
objective= cp.Minimize(cp.norm(P-X))
prob = cp.Problem(objective,constraints)
prob.solve()
print(X.value, prob.value)