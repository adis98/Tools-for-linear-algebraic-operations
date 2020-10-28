import numpy as np
np.set_printoptions(precision=4,suppress=True)
n = int(input('enter the dimension of square matrix A'))
A = np.zeros((n,n))
U = np.zeros((n,n))
H = np.zeros((n,n))


def householder(V,n,N):
    I = np.zeros((n,n))
    for i in range(n):
        I[i][i] = 1
    B = 2.0/(V.T.dot(V))
    temp = V.dot(V.T)
    H = I - B*temp
    P = np.zeros((N,N))
    start = N-n
    for i in range(n):
        for j in range(n):
            P[i+start][j+start] = H[i][j]
    for i in range(N):
        for j in range(N):
            if(i < start or j < start):
                if(i == j):
                    P[i][j] = 1
                else:
                    P[i][j] = 0
    return P

print('enter A elements')
for i in range(n):
    for j in range(n):
        A[i][j] = float(input())
        U[i][j] = A[i][j]
        if(i == j):
            H[i][j] = 1
        else:
            H[i][j] = 0
for i in range(n-1):
    X = np.zeros((n-i,1))
    for j in range(i,n):
        X[j-i] = U[j][i]
    e1 = np.zeros((n-i,1))
    e1[0] = 1
    X_norm_sq = X.T.dot(X)
    X_norm = X_norm_sq**0.5
    alpha = 0.0
    V = np.zeros((n-i,1))
    if (X[0] < 0):
        alpha = X_norm
    elif(X[0] >= 0):
        alpha = -X_norm
    print('alpha: ',alpha)
    V = X + alpha*e1
    print('V: ',V)
    H_temp = householder(V,n-i,n)
    H = H.dot(H_temp)
    U = H_temp.dot(U)
    print('H'+str(i+1)+':')
    print(H_temp)
    print('A'+str(i+1)+':')
    print(U)
Q = H
R = U
print('Q:')
print(Q)
print('R:')
print(R)
