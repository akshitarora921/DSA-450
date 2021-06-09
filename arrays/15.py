# next permutation

nums = [3, 2, 1]
flag = True
for i in range(len(nums)-2, -1, -1):
    if nums[i+1] > nums[i]:
        # print("ypyp")
        if i == len(nums)-2:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
        if i < len(nums)-1:
            # print(i)
            for j in range(len(nums)-1, i-1, -1):

                if nums[j] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
            b = nums[i+1:]
            b.sort()
            nums[:] = nums[:i+1]+b
            flag = False
        break

if flag:
    nums.sort()
print(nums)
