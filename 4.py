# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# russian flag problem

ip = [0, 1, 2, 0, 1, 0, 2]

hs = {}
for i in ip:
    if i in hs.keys():
        hs[i] += hs[i]
    else:
        hs[i] = 1
op = []
for i in hs.keys():
    for j in range(hs[i]):
        op.append((i))
print(op)
