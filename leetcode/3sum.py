"""
class Solution:
    def threeSum(self, nums):
        arr = sorted(nums)
        result = []
        for i in range(len(arr) - 1):
            left, right = i + 1, i + 2
            print(f'i: {i}, left: {left}, right: {right}')
            while left < right and right < len(arr):
                curr_sum = arr[i] + arr[left] + arr[right]
                print(i, left, right)
                print(f'arr[i]: {arr[i]}, arr[left]: {arr[left]}, arr[right]: {arr[right]} = ', curr_sum)
                if curr_sum == 0:
                    result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
        print(result)

"""
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        print(nums)
        for ind in range(len(nums)-2):
            # skips duplicate triplet
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            
            left, right = ind + 1, len(nums) - 1
            # print(left, right)
            while left < right:
                # print(left, right)
                curr_sum: int = nums[ind] + nums[left] + nums[right] 
               # skips duplicate value
                while left < right and nums[left] == nums[left + 1]:
                   left += 1
                # skips duplicate value
                while right > left and nums[right] == nums[right - 1]:
                    right -=  1

                if curr_sum == 0:
                   result.append([nums[ind], nums[left], nums[right]])
                
                left += 1
                right -= 1
                # if curr_sum < 0:
                #     left += 1
                # else:
                #     right -= 1
        print(result)

nums = [-1,0,1,2,-1,-4]
nums = [0, 0, 0]
nums = [1,-1,-1,0]
a = Solution()
a.threeSum(nums)
