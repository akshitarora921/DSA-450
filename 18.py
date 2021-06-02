# Count pairs with given sum

arr = [48, 24, 99, 51, 33, 39, 29, 83, 74, 72, 22, 46, 40, 51, 67, 37, 78, 76, 26, 28, 76, 25, 10,
       65, 64, 47, 34, 88, 26, 49, 86, 73, 73, 36, 75, 5, 26, 4, 39, 99, 27, 12, 97, 67, 63, 15, 3, 92, 90]
k = 50
ans = 0

   
count_arr = [0]*10000000
for i in arr:
    count_arr[i % 6] += 1

for i in range(len(arr)):
    ans += count_arr[k-arr[i]]

    if (k-arr[i]) == arr[i]:
        ans -= 1

print(int(ans/2))


# basic solution
# n = len(arr)
# for i in range(n):
#     for j in range(i+1, n):
#         if arr[i]+arr[j] == k:
#             ans += 1

# print(ans)
