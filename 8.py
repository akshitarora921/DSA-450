# find Largest sum contiguous Subarray [V. IMP]
# kadane problem

ar = [-47, 43, 94, -94, -93, -59, 31, -86]

# basic solution
temp = 0
largest_sum = 0
for i in ar:
    temp += i
    if temp > largest_sum:
        largest_sum = temp
    else:
        if temp < 0:
            temp = 0
print(largest_sum)

# dp
# max_so_far = ar[0]
# curr_max = ar[0]

# for i in range(1, len(ar)):  # saved one iteration of loop
#     curr_max = max(ar[i], curr_max+ar[i])
#     max_so_far = max(max_so_far, curr_max)
Arr
# print(max_so_far)
