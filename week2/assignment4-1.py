def twoSum(nums, target):
    mapping = {}
    # your code here
    for i in range(len(nums)):
        diff = target - nums[i]
        mapping[diff] = i
    for j in range(len(nums)):
        if (mapping[nums[j]]):
            return [j,mapping[nums[j]]]
        else:
            return 0
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
