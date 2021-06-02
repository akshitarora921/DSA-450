# Reverse the array

ip = [1, 2, 3, 4, 5]

# 1st method
# ip.reverse()
# print(ip)

# 2nd method
# op = []
# for i in range(len(ip)-1, -1, -1):
#     op.append(ip[i])
# print(op)

# 3rd method
# for i in range(0, len(ip)//2):
#     ip[i], ip[len(ip)-1-i] = ip[len(ip)-1-i], ip[i]

# print(ip)

# 4th method
print(ip[::-1])
