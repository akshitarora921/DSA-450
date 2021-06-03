# spiral traversal
r = 3
c = 4
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

top = 0
left = 0
bottom = r-1
right = c-1
dir = 0
# 0 means left to right
# 1 means top to bottom
# 2 means right to left
# 3 means bottom to top


while(top <= bottom and left <= right):
    if dir == 0:
        for i in range(left, right+1):
            print(matrix[top][i], end=" ")
        top += 1
    elif dir == 1:
        for i in range(top, bottom+1):
            print(matrix[i][right], end=" ")
        right -= 1
    elif dir == 2:
        for i in range(right, left-1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1
    elif dir == 3:
        for i in range(bottom, top-1, -1):
            print(matrix[i][left], end=" ")
        left += 1
    dir = (dir+1) % 4
