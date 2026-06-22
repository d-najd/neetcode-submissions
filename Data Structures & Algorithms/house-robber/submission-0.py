class Solution:
    
    
    def rob(self, nums: List[int]) -> int:
        while len(nums) > 3:
            first = nums[0] + nums[2]
            second = max(nums[0] + nums[3], nums[1] + nums[3])
            nums = [first, second] + nums[4:]
            print(nums)
        if (len(nums) == 1):
            return nums[0]
        elif (len(nums) == 2):
            return max(nums[0], nums[1])
        else:
            return max(nums[0] + nums[2], nums[1])

