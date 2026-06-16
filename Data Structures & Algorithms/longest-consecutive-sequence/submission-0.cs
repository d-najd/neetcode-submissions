public class Solution {
    public int LongestConsecutive(int[] nums) {
        var set = nums.ToHashSet();

        int largestCount = 0;
        while (set.Count != 0)
        {
            int curLargest = 0;
            
            int curElement = set.First();
            int curTemp = curElement;

            while (true)
            {
                if (set.Remove(curTemp++))
                {
                    curLargest++;
                }
                else
                {
                    break;
                }
            }

            curTemp = curElement;

            while (true)
            {
                if (set.Remove(curTemp--))
                {
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
