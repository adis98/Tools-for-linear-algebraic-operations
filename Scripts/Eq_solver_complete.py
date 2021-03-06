#solving Ax = b for partial pivoting
import numpy as np
np.set_printoptions(precision=4,suppress=True)
n = int(input('enter the dimension of X'))
x = np.zeros((n,1))
b = np.zeros((n,1))
p = np.zeros((n,n))
q = np.zeros((n,n))
l = np.zeros((n,n))
u = np.zeros((n,n))
y = np.zeros((n,1))
z = np.zeros((n,1))
w = np.zeros((n,1))
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
print('enter p')
for i in range(n):
    for j in range(n):
        p[i][j] = float(input())
print('enter q')
for i in range(n):
    for j in range(n):
        q[i][j] = float(input())
        
z = p.dot(b)
for i in range(n):
    temp = z[i]
    for j in range(i):
        temp -=l[i][j]*w[j]
    w[i] = temp/l[i][i]
print('Sol to Ly = b')
print(w)

for i in range(n-1,-1,-1):
    temp = w[i]
    for j in range(n-1,i,-1):
        temp -=u[i][j]*y[j]
    y[i] = temp/u[i][i]
print('Sol to Ux = y')
print('sol to Q\'x = y')
x = q.dot(y)
print(x)
