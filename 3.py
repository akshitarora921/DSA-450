# Find the "Kth" max and min element of an array

ip_k = 6
ip_ar = [1, 2, 3, 4, 5, 6]

ip_ar.sort()

print(ip_ar[ip_k-1], ip_ar[len(ip_ar)-ip_k])
