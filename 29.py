# Trapping Rain Water

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)

# dual pointer Technique
# l = 0
# r = n-1
# lmax = 0
# rmax = 0
# water = 0
# while l <= r:
#     if arr[l] <= arr[r]:
#         if arr[l] >= lmax:
#             lmax = arr[l]
#         else:
#             water += lmax-arr[l]
#         l += 1
#     else:
#         if arr[r] >= rmax:
#             rmax = arr[r]
#         else:
#             water += rmax-arr[r]
#         r -= 1


# print(water)

# stored prfix sum list
# water = 0
# maxa = arr[0]
# leftMax = [arr[0]]
# for i in range(1, n):
#     if arr[i] > maxa:
#         leftMax.append(arr[i])
#         maxa = arr[i]
#     else:
#         leftMax.append(maxa)

# maxa = arr[n-1]
# rightMax = [0]*n
# for i in range(n-1, -1, -1):
#     if arr[i] > maxa:
#         rightMax[i] = arr[i]
#         maxa = arr[i]
#     else:
#         rightMax[i] = maxa

# for i in range(n):
#     water += min(leftMax[i], rightMax[i])-arr[i]
# print(water)


# first try
# b = list(set(arr))
# b.sort()
# nn = len(b)
# maxx = b[nn-1]
# second_max = b[nn-2]
# print(maxx, second_max)
# current_max = 0
# total_max = 0

# for i in range(n):
#     if arr[i] < maxx:
#         current_max += second_max-arr[i]
#         print('cm', current_max)
#     else:
#         print("No")
#         total_max = max(total_max, current_max)
#         current_max = 0

# print(total_max)
