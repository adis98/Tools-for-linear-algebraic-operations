import numpy as np
np.set_printoptions(precision=4,suppress=True)
m = int(input('enter rowdim of A'))
n = int(input('enter coldim of A'))
L = np.identity(m)
U = np.zeros((m,n))
r = min(m,n)
A = np.zeros((m,n))
print('enter A')
for i in range(m):
    for j in range(n):
        A[i][j] = float(input())
        U[i][j] = A[i][j]
for i in range(r):
    L_temp = np.identity(m)
    M_inv = np.identity(m)
    pivot = U[i][i]
    for j in range(i+1,m):
        L_temp[j][i] = -U[j][i]/pivot
        M_inv[j][i] = -L_temp[j][i]
    L = L.dot(M_inv)
    U = L_temp.dot(U)
    print('M'+str(i+1)+':')
    print(L_temp)
    print('A'+str(i+1)+':')
    print(U)
print('L:')
print(L)
print('U:')
print(U)
    
