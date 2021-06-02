# Write a program to cyclically rotate an array by one.

a = [1, 2]

rotate_by = 3

# temp = a[len(a)-1]

# for i in range(len(a)-1, 0, -1):
#     a[i] = a[i-1]

# a[0] = temp
temp = a[len(a)-1:]
# op=[]
temp2 = a[0:len(a)-1]
# temp = a[len(a)-rotate_by:]
# op=[]
print(temp)
print(temp+temp2)
# temp = temp + a[0:len(a)-rotate_by]
# for i in range(len(a)-rotate_by):
#     temp.append(a[i])

# for i in temp:
#     print(i, end=" ")

# answer

a[:] = a[-rotate_by:] + a[:-rotate_by]
