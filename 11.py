# Find the Duplicate Number
nums = [1, 2, 2, 4, 3, 6, 7, 8]

a = set()
for i in nums:
    if i in a:
        print(i)
    else:
        a.add(i)

# dict={}
# for i in nums:
#     if i in dict.keys():
#         return i
#     else:
#         dict[i]=1
#


# Approach 3: Floyd's Tortoise and Hare
# https://leetcode.com/problems/find-the-duplicate-number/solution/
# hare = tortoise = nums[0]

# while True:
#     tortoise = nums[tortoise]
#     hare = nums[nums[hare]]

#     if tortoise==hare:
#         break

# tortoise = nums[0]

# while tortoise !=hare:
#     tortoise = nums[tortoise]
#     hare=nums[hare]

# return hare
