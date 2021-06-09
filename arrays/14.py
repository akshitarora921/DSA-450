# Merge Intervals
intervals = [[1, 4], [1, 5]]

# [1, 4], [3, 5]
intervals.sort()
ans = []
comp = intervals[0]

for interval in intervals:
    if interval[0] <= comp[1]:
        comp[1] = max(comp[1], interval[1])
    else:
        ans.append(comp)
        comp = interval

ans.append(comp)
print(ans)
