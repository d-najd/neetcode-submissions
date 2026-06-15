public class Solution {
    List<string> temp = new List<string>();

    public List<string> GenerateParenthesis(int n) {
        GenerateTest("", 0, n);
        return temp;
    }

    private void GenerateTest(String cur, int curOpen, int depthRemaining) {
        Console.WriteLine($"{cur} {curOpen} {depthRemaining}");
        if (depthRemaining == 0) {
            while(curOpen > 0) {
                cur += ")";
                curOpen--;
            }
            temp.Add(cur);
            return;
        }

        if (curOpen > 0) {
            GenerateTest(cur + ")", curOpen - 1, depthRemaining);
        }

        GenerateTest(cur + "(", curOpen + 1, depthRemaining - 1);
    }
}
