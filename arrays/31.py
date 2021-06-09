# Smallest subarray with sum greater than x
a = [1, 4, 45, 6, 0, 19]
n = len(a)
x = 51
ans = n
left = 0
cur_sum = 0
for i in range(left, n):
    cur_sum += a[i]

    while cur_sum > x:
        ans = min(ans, i+1-left)
        cur_sum -= a[left]
        left += 1

print(ans)
