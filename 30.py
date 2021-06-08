# Chocolate Distribution Problem

N = 8, M = 5 #M is number of stdents
A = [3, 4, 1, 9, 56, 7, 9, 12]
A.sort()
cuu_dif = A[N-1]-A[0]
for i in range(N-M+1):
    cuu_dif = min(cuu_dif, A[M+i-1]-A[i])

print(cuu_dif)
