class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
        let low = 0;
        let high = nums.length - 1;

        while (low <= high) {
            const mid = Math.floor((low + high) / 2);

            if (nums[mid] === target) {
                return mid;
    } else if (nums[mid] < target) {
      low = mid + 1; // Discard the left half
    } else {
      high = mid - 1; // Discard the right half
    }
  }
  return -1; // Target not found    }
}
}
