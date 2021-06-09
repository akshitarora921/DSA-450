# Subarray with 0 sum
arr = [2, -3, 1, 6]
n = len(arr)
sum = 0
s = {}
max_len = 0
for i in range(n):
    sum += arr[i]

    if sum == 0:
        max_len = i+1
    else:
        if sum in s.keys():
            max_len = max(max_len, i-s[sum])
        else:
            s[sum] = i
print(s)
print(max_len)

# print(False)
# a.sort()
# i = 0
# sum = 0
# if min(a) <= 0:
#     while i < len(a):
#         sum += a[i]
#         print(sum)
#         if sum == 0:
#             print(True)
#             break
#         i += 1
