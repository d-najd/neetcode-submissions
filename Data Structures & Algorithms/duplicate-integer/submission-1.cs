public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> test = new HashSet<int>(nums);

        if (test.Count != nums.Length) {
            return true;
        }
        return false;
    }
}
