def two_sum(nums,target):
    complement_map = {}

    for i,num in enumerate(nums):
        if target - num in complement_map:
            return [complement_map[target-num],i]
        complement_map[num] = i

#example usage:
nums = [2,7,11,15]
target = 17
print(two_sum(nums,target))

