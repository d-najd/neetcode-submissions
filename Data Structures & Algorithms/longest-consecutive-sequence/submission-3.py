import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)

        if len(nums) == 0:
            return 0

        #prev = heapq.heappop(nums)
        cur_count = 1
        max_count = 1

        prev = heapq.heappop(nums)

        while len(nums) != 0:
            cur = heapq.heappop(nums)
            #print(f"comparing {prev} {cur} {cur_count}")
            if prev + 1 == cur:
                cur_count += 1
            elif prev == cur:
                pass
            else:
                if cur_count > max_count:
                    max_count = cur_count
                cur_count = 1

            prev = cur
        if cur_count > max_count:
            max_count = cur_count
        """
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                cur_count += 1
            else:
                if cur_count > max_count:
                    max_count = cur_count
                cur_count = 1
        if cur_count > max_count:
            max_count = cur_count
        """
       # for i in range(len(heap)-1):
       #     heap[0]

        return max_count