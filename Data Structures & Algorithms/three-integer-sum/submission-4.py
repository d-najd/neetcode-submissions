import bisect
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        nums.sort()


       # -4, -1, -1, 0, 1, 2

        for lp, lv in enumerate(nums):
            if lp != 0 and nums[lp - 1] == lv:
                continue
            
            mp = lp+1
            rp = len(nums) - 1
            while mp < rp:
                cur_result = lv + nums[mp] + nums[rp]

                if cur_result == 0:
                    if nums[mp-1] != nums[mp] or rp + 1 >= len(nums) or nums[rp+1] != nums[rp]:
                        result.append([lv, nums[mp], nums[rp]])
                    rp -= 1
                    mp += 1
                elif cur_result > 0:
                    rp -= 1
                else:
                    mp += 1


        return result