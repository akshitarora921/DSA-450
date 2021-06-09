# Find factorial of a large number

n = 897
sum = 1
for i in range(1, n//2+1):
    sum *= i*(n+1-i)
print(sum)
