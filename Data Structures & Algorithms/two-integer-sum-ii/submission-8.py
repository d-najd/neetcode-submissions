class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (True):
            sum = numbers[l] + numbers[r]
            if (sum == target):
                return [l+1, r+1]
            elif (target > sum):
                l = l+1
            else:
                r = r-1

        return [-1,-1]