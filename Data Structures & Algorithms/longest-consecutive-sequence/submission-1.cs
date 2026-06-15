public class Solution {
    public int LongestConsecutive(int[] nums) {
        var set = nums.ToHashSet();

        int largestCount = 0;
        while (set.Count != 0)
        {
            int curLargest = 1;
            
            int curElement = set.First();
            set.Remove(curElement);
            int curTemp = curElement + 1;

            while (true)
            {
                if (set.Remove(curTemp))
                {
                    curLargest++;
                    curTemp++;
                }
                else
                {
                    break;
                }
            }

            curTemp = curElement - 1;

            while (true)
            {
                if (set.Remove(curTemp))
                {
                    curTemp--;
                    curLargest++;
                }
                else
                {
                    break;
                }
            }

            if (curLargest > largestCount)
            {
                largestCount = curLargest;
            }
        }

        return largestCount;
    }
}
