# Triplet Sum in Array
a = [1, 2, 3, 4, 5]
n = len(a)
X = 9

# double pointer approach
a.sort()

for i in range(0, n-2):
    l = i+1
    r = n-1
    while l < r:
        if a[i]+a[l]+a[r] == X:
            print("True")
            exit()
        elif a[i]+a[l]+a[r] < X:
            l += 1
        else:
            r -= 1
print('False')
# return count
# for i in range(n):
#     if a[i]>X:
#         continue
#     for j in range(n):
#         if a[j]>X-a[i]:
#             continue
#         else:
#             c=X-a[i]-a[j]
#             if c in a:
#                 if a[i]!=a[j]!=c:
#                     count+=1
# print(count)
