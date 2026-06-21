class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        checked: set[int] = set()
        
        max = 0
        for curHeight in heights:  


            curCount = 0
            for p in heights:
                if (p >= curHeight): 
                    curCount += 1
                else:
                    sum = curCount * curHeight
                    if (sum > max):
                        max = sum
                    curCount = 0
            sum = curCount * curHeight
            if (sum > max):
                max = sum
        return max