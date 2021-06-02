# Merge Without Extra Space
import math
n = 4
m = 5
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

# gap method
gap = math.ceil((n+m)/2)
print(gap)
while True:

    # print(gap)
    front = 0
    end = gap
    print(gap)
    while end < n+m:
        print(arr1, arr2)
        # print(front, end)
        if end < n-1:
            if arr1[front] > arr1[end]:
                temp = arr1[front]
                arr1[front] = arr1[end]
                arr1[end] = temp
        if front < n-1 and end > n-1:

            if arr1[front] > arr2[n-end]:
                temp = arr1[front]
                arr1[front] = arr2[n-end]
                arr2[n-end] = temp
        if front > n and end > n:
            if arr2[n-front] > arr2[n-end]:
                temp = arr2[n-front]
                arr2[n-front] = arr2[n-end]
                arr2[n-end] = temp
        front += 1
        end += 1
    if gap == 1:
        break
    gap = math.ceil(gap/2)


# greedy iter method space-complexity O(1)
# for i in range(n):
#     if arr1[i] > arr2[0]:
#         temp = arr1[i]
#         arr1[i] = arr2[0]
#         arr2[0] = temp
#         arr2.sort()

print(arr1, arr2)


# this basic
# i = 0
# j = 0
# ans = []
# while i < n and j < m:
#     if arr1[i] < arr2[j]:
#         ans.append(arr1[i])
#         i += 1
#     else:
#         # print(arr1[i] < arr2[j])
#         ans.append(arr2[j])
#         j += 1

# while i < n:
#     ans.append(arr1[i])
#     i += 1
# while j < m:
#     ans.append(arr2[j])
#     j += 1
# arr1[:] = ans[:n]
# arr2[:] = ans[n:]

# print(arr1)
# print(arr2)
