public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] returnArr = new int[nums.Length];
        int detected0Pos = -1;
        int sumVal = 0;
        bool sumValSet = false;

        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] == 0)
            {
                if (detected0Pos != -1)
                {
                    for (int b = 0; b < nums.Length; b++)
                    {
                        returnArr[b] = 0;
                    }

                    return returnArr;
                }
                detected0Pos = i;

            }
            else
            {
                if (!sumValSet)
                {
                    sumVal = nums[i];
                    sumValSet = true;
                }
                else
                {
                    sumVal *= nums[i];
                }
                continue;
            }
        }

        if (detected0Pos != -1)
        {
            for (int i = 0; i < nums.Length; i++)
            {
                if (detected0Pos == i)
                {
                    returnArr[i] = sumVal;
                    continue;
                }
                returnArr[i] = 0;
            }

        }
        else
        {
            for (int i = 0; i < nums.Length; i++)
            {
                returnArr[i] = sumVal / nums[+i];
            }
        }
        
        return returnArr;
    }
}
