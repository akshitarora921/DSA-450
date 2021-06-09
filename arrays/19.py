# find common elements In 3 sorted arrays

n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]


# for i in range(max(n1,n2,n3)):
ans = []
i = j = k = 0
while i < n1 and j < n2 and k < n3:
    if A[i] == B[j] and B[j] == C[k]:
        ans.append(A[i])
        i += 1
        j += 1
        k += 1

    elif A[i] > B[j]:
        j += 1
    elif A[i] > C[k]:
        k += 1
    else:
        i += 1
print(sorted(list(set(ans))))

# ans = set()

# for i in range(n1):
#     if A[i] in B and A[i] in C:
#         ans.add((A[i]))

# print(sorted(list(ans)))
