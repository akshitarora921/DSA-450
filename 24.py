# Longest consecutive subsequence

N = 5
arr = [1, 2, 6, 4, 5]

# set approach
check_set = set(arr)
count = 0
maxCount = 0
for i in range(N):
    if arr[i]-1 in check_set:
        continue
    else:
        number = arr[i]
        while(number in check_set):
            number += 1
            count += 1

        maxCount = max(maxCount, count)
        count = 0
print(maxCount)
# Naive Approach
# arr = list(set(arr))
# arr.sort()
# count = 1
# maxCount = 0
# print(arr)
# for i in range(1, len(arr)):
#     if arr[i] == arr[i-1]+1:
#         count += 1
#     else:
#         count = 1
#     maxCount = max(maxCount, count)
# print(maxCount)


# count = set()
# for i in range(N):
#     if arr[i]-1 in arr or arr[i]+1 in arr:
#         count.add(arr[i])
# print(count)
