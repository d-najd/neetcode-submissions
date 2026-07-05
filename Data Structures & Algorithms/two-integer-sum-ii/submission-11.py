class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1

        while rp > lp:
            lv = numbers[lp]
            rv = numbers[rp]

            sum = lv + rv

            if sum == target:
                return [lp+1, rp+1]
            elif sum > target:
                rp -= 1
            else:
                lp += 1
    
        return -1