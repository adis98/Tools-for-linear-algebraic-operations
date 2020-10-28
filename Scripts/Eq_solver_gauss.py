#solving equations of the form Ax = b; ie LUx = b
import numpy as np
np.set_printoptions(precision=4,suppress=True)
n = int(input('enter the dimension of X'))
x = np.zeros((n,1))
b = np.zeros((n,1))
l = np.zeros((n,n))
u = np.zeros((n,n))
y = np.zeros((n,1))
print('enter b')
for i in range(n):
    b[i] = float(input())
print('enter l')
for i in range(n):
    for j in range(n):
        l[i][j] = float(input())
print('enter u')
for i in range(n):
    for j in range(n):
        u[i][j] = float(input())
for i in range(n):
    temp = b[i]
    for j in range(i):
        temp -=l[i][j]*y[j]
    y[i] = temp/l[i][i]
print('Sol to Ly = b')
print(y)

for i in range(n-1,-1,-1):
    temp = y[i]
    for j in range(n-1,i,-1):
        temp -=u[i][j]*x[j]
    x[i] = temp/u[i][i]
print('Sol to Ux = y')
print(x)
