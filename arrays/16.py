# Count Inversion
arr = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392,
       105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323]

ans = 0
temp = [0]*len(arr)
n = len(arr)


def merge(arr, temp, left, mid, right):
    i = left
    j = mid+1
    k = left
    invert_count = 0
    while (i <= mid) and (j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            invert_count += mid-i+1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    # arr[:] = temp[:]

    return invert_count


def mergeSort(arr, temp, left, right):
    invert_count = 0
    if left < right:
        mid = (right+left)//2
        invert_count += mergeSort(arr, temp, left, mid)
        invert_count += mergeSort(arr, temp, mid+1, right)
        invert_count += merge(arr, temp, left, mid, right)

    return invert_count


print(mergeSort(arr, temp, 0, n-1))
# take alot of time
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         if arr[i] > arr[j]:
#             ans += 1
# print(ans)
