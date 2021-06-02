# Find the maximum and minimum element in an array

ip = [1, 2, 3, 4, 5, 6]

# 1st method
# min = max = ip[0]
# for i in ip:
#     if max < i:
#         max = i
#     if min > i:
#         min = i

# print(min, max)

# 2nd method
ip.sort()
print(ip[0], ip[len(ip)-1])
