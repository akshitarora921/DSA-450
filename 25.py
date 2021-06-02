# Given an array of size n and a number k, find all elements that appear more than n/k times

arr = [3, 1, 2, 2, 1, 2, 3, 3]
n = len(arr)
k = 2

has_set = {}
for i in range(n):
    if arr[i] in has_set.keys():
        has_set[arr[i]] += 1
    else:
        has_set[arr[i]] = 1

for i in has_set.keys():
    if has_set[i] > n//k:
        print(i, end=" ")
