def twoSum(nums,target):
    num_map={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in num_map:
            return[num_map[complement],i]
        num_map[num]=i
    return []
nums=[2,7,11,15]
num=[3,2,4]
nums1=[3,3]
target=6
print(twoSum(nums,target))
print(twoSum(num,target))
print(twoSum(nums1,target))