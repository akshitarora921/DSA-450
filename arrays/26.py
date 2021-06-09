# Maximum profit by buying and selling a share at most twice

price = [2, 30, 15, 10, 8, 25, 80]
n = len(price)
profit = 0
for i in range(1, n):
    if price[i] > price[i-1]:
        profit += price[i]-price[i-1]
print(profit)

# minVal = price[0]
# maxVal = price[0]
# ans = 0

# for i in range(1, len(price)):
#     if price[i] < maxVal and price[i] > minVal:
#         continue
#     elif price[i] < minVal:
#         ans += maxVal-minVal
#         minVal = price[i]
#         maxVal = 0
#     elif price[i] > maxVal:
#         maxVal = price[i]
#     if i == len(price)-1:
#         ans += maxVal-minVal
#     # print(minVal, maxVal, ans)
# print(ans)
