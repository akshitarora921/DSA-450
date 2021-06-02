# # Minimum no. of Jumps to reach end of an array
a = [2, 3, 1, 1, 4]
n = len(a)

# if a[0]==0 and n==1:
#     print(0)
#     exit()
# farthest = a[0]
# steps=a[0]
# jump=1
# curr_end=a[0]

# for i in range(1,n):
#     if i==n-1:
#         print(jump)
#     farthest = max(farthest, i+a[i])
#     if i==curr_end:
#         jump+=1
#         curr_end=farthest

max_rechable = a[0]
jump = 1
step_possible = a[0]
for i in range(1, n):
    if i == n-1:
        print(jump)
    max_rechable = max(max_rechable, i+a[i])

    step_possible -= 1

    if step_possible == 0:
        if i >= max_rechable:
            print(-1)
        step_possible = max_rechable-i
        jump += 1
