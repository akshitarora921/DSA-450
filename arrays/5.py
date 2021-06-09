# Move all the negative elements to one side of the array

ip = [1, 2, -1, 2, 4, -2, -5, -7]

low = 0
for i in range(0, len(ip)//2-1):
    if ip[i] < 0:
        temp = ip[low]
        ip[low] = ip[i]
        ip[i] = temp
        low = low+1
    if ip[len(ip)-1-i] < 0:
        temp = ip[low]
        ip[low] = ip[len(ip)-1-i]
        ip[len(ip)-1-i] = temp
        low = low+1
    print(ip)
print(ip)
