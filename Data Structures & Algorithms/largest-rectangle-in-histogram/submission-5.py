class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        checked: set[int] = set()
        
        hLen = len(heights)

        max = 0
        for curHeight in heights:  
            if (curHeight * hLen < max):
                continue 

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