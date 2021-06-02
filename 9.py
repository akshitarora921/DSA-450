# Minimise the maximum difference between heights [V.IMP]

k = 2
n = 4
arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
# arr = [1, 2, 3]

arr.sort()
ans = arr[n-1]-arr[0]
min_num = arr[0]+k
max_num = arr[n-1]-k

for i in range(1, n):
    if arr[i] < k:
        continue
    else:
        mn = min(min_num, arr[i-1]-k)
        mx = max(max_num, arr[i]+k)
        ans = min(ans, mx-mn)

print(ans)

# max_element = max(arr)-k
# for i in range(len(arr)):
#     if arr[i]+k <= max_element:
#         if max_element <= arr[i]+k:
#             max_element = arr[i]+k
#             arr[i] -= k
#         else:
#             arr[i] += k
#     else:
#         arr[i] -= k

# print(arr)
# print(max(arr)-min(arr))
# print(arr)
# max_element = max(arr)
# min_element = min(arr)
# for i in range(len(arr)):
#     # max_element = max(arr)
#     if arr[i]+k > max_element:
#         if arr[i]-k < min_element:
#             arr[i] += k
#             max_element = arr[i]
#         else:
#             arr[i] -= k
#             # max_element = arr[i]+k
#     else:
#         arr[i] += k

# print(arr)
# print(max(arr)-min(arr))
