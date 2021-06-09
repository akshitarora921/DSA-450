# Rearrange array in alternating positive & negative items with O(1) extra space

prices = [1, 2, 3, -4, -1, 4]
max_value = prices[0]
min_value = prices[0]
ans = 0

for i in range(1, len(prices)):
    if prices[i] < min_value:
        min_value = prices[i]
        max_value = 0
    if prices[i] > max_value:
        max_value = prices[i]
        # max_value = 0
    ans = max(ans,max_value-min_value)
    # print(max_value, min_value)
print(ans)