public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.Length; i++) {
            for (int b = i + 1; b < nums.Length; b++) {
                if (nums[i] + nums[b] == target) {
                    return new[] { i, b };
                }
            }
        }
        return null;
    }
}
