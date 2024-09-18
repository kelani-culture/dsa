# def findpairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 print(i, j)
            
# mlst = [1, 2, 3, 4, 5, 6]
# findpairs(mlst, 6)

def two_sum(nums, target):
    seen = {}
 
    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))