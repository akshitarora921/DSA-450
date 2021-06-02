# kadane Problem

a = [1, 2, 3, -2, 5]
curr_max = 0
total_max = 0

for i in a:
    curr_max += i
    total_max = max(total_max, curr_max)
    if curr_max < 0:
        curr_max = 0

print(total_max)
