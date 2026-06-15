public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] returnArr = new int[nums.Length];

        for (int i = 0; i < nums.Length; i++)
        {
            bool set = false;
            for (int b = 0; b < nums.Length; b++)
            {
                if (i == b)
                {
                    continue;
                }

                if (!set)
                {
                    returnArr[i] = nums[b];
                    set = true;
                    continue;
                }

                returnArr[i] *= nums[b];
            }
        }

        return returnArr;
    }
}
