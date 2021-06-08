# Three way partitioning

n = 5
array = [1, 2, 3, 3, 4]
a, b = 1, 2


left = 0
right = len(array)-1
i = 0
while i <= right:
    # print(i)
    # left =i+1
    # right = len(array)-1
    # if left<right:
    if array[i] < a:
        temp = array[i]
        array[i] = array[left]
        array[left] = temp
        left += 1
        i += 1
    elif array[i] > b:
        temp = array[i]
        array[i] = array[right]
        array[right] = temp
        right -= 1
    else:
        i += 1

print(array)
