import numpy as np
np.set_printoptions(precision=4,suppress=True)
m1 = int(input('enter rowdim of A'))
n1 = int(input('enter coldim of A'))
m2 = int(input('enter rowdim of B'))
n2 = int(input('enter coldim of B'))
if( m2 != n1):
    print('error')
    exit()

a = np.zeros((m1,n1))
b = np.zeros((m2,n2))
print('enter A')
for i in range(m1):
    for j in range(n1):
        a[i][j] = float(input())
print('enter b')
for i in range(m2):
    for j in range(n2):
        b[i][j] = float(input())
print('result:',a.dot(b))
