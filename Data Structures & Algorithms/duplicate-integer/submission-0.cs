public class Solution {
    public bool hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.Length; i++) {
            for (int b = i+1; b < nums.Length; b++) {
                if (nums[i] == nums[b]) {
                    return true;
                }
            }
        }
        return false;
    }
}
