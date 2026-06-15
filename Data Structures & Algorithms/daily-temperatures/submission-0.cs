public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.Length];
        Stack<Tuple<int, int>> stack = new();

        for (int i = temperatures.Length - 1; i >= 0; i--) {
            if (stack.Count > 0) {
                while(stack.Count > 0 && temperatures[i] >= stack.Peek().Item2) {
                    stack.Pop();
                }
                if (stack.Count > 0) {
                    result[i] = stack.Peek().Item1 - i;
                }
            } 
            stack.Push(new (i, temperatures[i]));
        }
        return result;
    }
}
