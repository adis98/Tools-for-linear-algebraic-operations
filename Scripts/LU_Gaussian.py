import numpy as np
np.set_printoptions(precision=4,suppress=True)
n = int(input('enter the dimension of square matrix A'))
A = np.zeros((n,n))
M = np.zeros((n,n))
M_inv = np.zeros((n,n))
L = np.zeros((n,n))
U= np.zeros((n,n))
print('enter the elements of A')
for i in range(n):
    for j in range(n):
        A[i][j] = float(input())
        U[i][j] = A[i][j]
        if(i == j):
            L[i][j] = 1
        else:
            L[i][j] = 0
for i in range(n-1):
    pivot = U[i][i]
    for k in range(n):
        for l in range(n):
            if(k == l):
                M[k][l] = 1
                M_inv[k][l] = 1
            else:
                M[k][l] = 0
                M_inv[k][l] = 0
    for j in range(i+1,n):
        M[j][i] = -U[j][i]/pivot
        M_inv[j][i] = U[j][i]/pivot
    U = M.dot(U)
    L = L.dot(M_inv)
    print('M',i+1,':')
    print(M)
    print('A',i+1,':')
    print(U)
print('L:')
print(L)
print('U:')
print(U)

solve = int(input('Do you want to solve an equation now?(1/0)'))
if(solve == 1):
    x = np.zeros((n,1))
    b = np.zeros((n,1))
    l = L
    u = U
    y = np.zeros((n,1))
    print('enter b')
    for i in range(n):
        b[i] = float(input())
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

    
        
        
