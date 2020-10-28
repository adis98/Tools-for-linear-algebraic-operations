import numpy as np
np.set_printoptions(precision=4,suppress=True)
n = int(input('enter the dimension of square matrix A'))
A = np.zeros((n,n))
P = np.zeros((n,n))
Q = np.zeros((n,n))
M = np.zeros((n,n))
M_inv = np.zeros((n,n))
L = np.zeros((n,n))
U= np.zeros((n,n))
def permut(i,j,n):
    temp = np.zeros((n,n))
    temp[i][j] = 1
    temp[j][i] = 1
    for k in range(n):
        if(k != i and k!= j):
            temp[k][k] = 1
    return temp
print('enter the elements of A')
for i in range(n):
    for j in range(n):
        A[i][j] = float(input())
        U[i][j] = A[i][j]
        if(i == j):
            L[i][j] = 1
            P[i][j] = 1
            Q[i][j] = 1
        else:
            L[i][j] = 0
            P[i][j] = 0
            Q[i][j] = 0

for i in range(n-1):
    mx_r = i
    mx_col = i
    for k in range(i+1,n):
        for l in range(i+1,n):
            if(abs(U[k][l])>abs(U[mx_r][mx_col])):
                mx_r = k
                mx_col = l
    Q_temp = permut(i,mx_col,n)
    Q = Q.dot(Q_temp)
    U = U.dot(Q_temp)
    print('AQ is:')
    print(U)
    P_temp = permut(i,mx_r,n)
    P = P_temp.dot(P)
    U = P_temp.dot(U)
    print('PAQ is:')
    print(U)
    for k in range(n):
        for l in range(n):
            if(k == l):
                M[k][l] = 1
                M_inv[k][l] = 1
            else:
                M[k][l] = 0
                M_inv[k][l] = 0
    pivot = U[i][i]
    for j in range(i+1,n):
        M[j][i] = -U[j][i]/pivot
        M_inv[j][i] = U[j][i]/pivot
    U = M.dot(U)
    L = L.dot(P_temp)
    L = L.dot(M_inv)
    print('Q'+str(i+1)+':')
    print(Q_temp)
    print('P'+str(i+1)+':')
    print(P_temp)
    print('M'+str(i+1)+':')
    print(M)
    print('A'+str(i+1)+':')
    print(U)
L = P.dot(L)
print('P:')
print(P)
print('Q:')
print(Q)
print('L:')
print(L)
print('U:')
print(U)

solve = int(input('Do you want to solve an equation now?(1/0)'))
if(solve == 1):
    x = np.zeros((n,1))
    b = np.zeros((n,1))
    p = P
    q = Q
    l = L
    u = U
    y = np.zeros((n,1))
    z = np.zeros((n,1))
    w = np.zeros((n,1))
    print('enter b')
    for i in range(n):
        b[i] = float(input())
            
    z = p.dot(b)
    for i in range(n):
        temp = z[i]
        for j in range(i):
            temp -=l[i][j]*w[j]
        w[i] = temp/l[i][i]
    print('Sol to Lw = pb')
    print(w)

    for i in range(n-1,-1,-1):
        temp = w[i]
        for j in range(n-1,i,-1):
            temp -=u[i][j]*y[j]
        y[i] = temp/u[i][i]
    print('Sol to Uy = w')
    print(y)
    print('sol to Q\'x = y')
    x = q.dot(y)
    print(x)

