# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# russian flag problem

ip = [0, 1, 2, 0, 1, 0, 2]

# hs = {}
# for i in ip:
#     if i in hs.keys():
#         hs[i] += hs[i]
#     else:
#         hs[i] = 1
# op = []
# for i in hs.keys():
#     for j in range(hs[i]):
#         op.append((i))
# print(op)

count_0 = 0
count_1 = 0
count_2 = 0
for i in ip:
    if i == 0:
        count_0 += 1
    elif i == 1:
        count_1 += 1
    else:
        count_2 += 1
i = 0
while count_0 > 0:
    ip[i] = 0
    i += 1
    count_0 -= 1
while count_1 > 0:
    ip[i] = 1
    i += 1
    count_1 -= 1
while count_2 > 0:
    ip[i] = 2
    i += 1
    count_2 -= 1

print(ip)
