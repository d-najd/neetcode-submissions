class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max_product = 1
        zero_index = -1
        
        for i, v in enumerate(nums):
            if v == 0:
                if zero_index != -1:
                    return [0 for i in range(len(nums))]
                zero_index = i
                continue
            
            max_product *= v
        
        result = []
        if zero_index != -1:
            for i in range(len(nums)):
                if i == zero_index:
                    result.append(max_product)
                    continue
                result.append(0)
            return result
        
        for v in nums:
            result.append(max_product // v)
        return result