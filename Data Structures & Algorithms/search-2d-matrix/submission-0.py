class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lp = 0
        rp = len(matrix) * len(matrix[0]) - 1
        while lp <= rp:
            mid = (rp + lp) // 2
            y = mid//len(matrix[0])
            x = mid - (y * len(matrix[0]))
            val = matrix[y][x]
            if target == val:
                return True
            elif target < val:
                rp = mid-1
            else:
                lp = mid+1
        return False