# Maximum Product Subarray

n = 10
arr = [8, -2, -2, 0, 8, 0, -6, -8, -6, -1]
maxProd = 1
# currmaxprod = 1
# for i in range(n):

#     currmaxprod = arr[i]*currmaxprod
#     maxProd = max(maxProd, currmaxprod)
#     if arr[i] == 0:
#         # temp =currmaxprod
#         currmaxprod = 1
#     if currmaxprod < 0:
#         currmaxprod *= -1
#         # maxProd = temp
#         # print("yoyo")

minVal = arr[0]
maxVal = arr[0]
maxProd = arr[0]

for i in range(1, n):
    if arr[i] < 0:
        temp = minVal
        minVal = maxVal
        maxVal = temp
    minVal = min(arr[i], arr[i]*minVal)
    maxVal = max(arr[i], arr[i]*maxVal)

    maxProd = max(maxProd, maxVal)


print(maxProd)
