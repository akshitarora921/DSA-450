# fMedian of 2 sorted arrays of different size
import math
a = [23, 26, 31, 35]
b = [3, 5, 7, 9, 11, 16]

n1 = len(a)
n2 = len(b)

low = 0
high = n1

while low <= high:
    partition_x = int((low+high)/2)
    partition_y = int((n1+n2+1)/2-partition_x)

    maxLeftX = -math.inf if partition_x == 0 else a[partition_x-1]
    minRightX = math.inf if partition_x == n1 else a[partition_x]

    maxLeftY = -math.inf if partition_y == 0 else b[partition_y-1]
    minRightY = math.inf if partition_y == n2 else b[partition_y]

    if maxLeftX <= minRightY and maxLeftY <= minRightX:
        if (n1+n2) % 2 == 0:
            print((max(maxLeftX, maxLeftY)+min(minRightX, minRightY))/2)
            break
        else:
            print(min(maxLeftX, maxLeftY))
            break
    elif maxLeftX > minRightY:
        high = partition_x-1
    else:
        low = partition_x+1


# basic approach
# c = a+b
# c.sort()
# n = len(c)
# if n % 2 == 0:
#     print((c[int((n+1)/2)]+c[int((n-1)/2)])/2)
# else:
#     print(c[n/2])
