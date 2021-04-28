import cvxpy as cp
import numpy as np
np.set_printoptions(precision=3)
n = 2
m = 2
P = np.array([[0.2050078785,0.7949921215],
              [0.7316819956,0.2683180044]])
sum_x=1
x = cp.Variable(shape=n)
y = P*x
c = np.sum(P*np.log2(P),axis=0)
I = c*x + cp.sum(cp.entr(y))
obj = cp.Minimize(-I)
constraints = [cp.sum(x) == sum_x,x >= 0]
prob = cp.Problem(obj,constraints)
prob.solve()
if prob.status=='optimal':
    states= prob.status
    C = prob.value
    x = x.value
else:
    states= prob.status
    C = np.nan
    x = np.nan
    
print('Problem status: ',states)
print('Optimal value of C = {:.4g}'.format(C))
print('Optimal variable x = \n', x)
