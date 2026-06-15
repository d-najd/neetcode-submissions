public class Solution {
    public bool IsValidSudoku(char[][] board) {
        HashSet<int> tempSet = new HashSet<int>(1000);
        HashSet<int> tempSet1 = new HashSet<int>(1000);
        HashSet<int> tempSet2 = new HashSet<int>(1000);


        for (int x = 0; x < 9; x++) {
            for (int y = 0; y < 9; y++) {
                if (board[x][y] != '.') {
                    int val = board[x][y] - '0';
                    if (!tempSet.Add(x * 10000 + val) ||
                        !tempSet.Add(y * 10000 + val * 31 * 210) ||
                        !tempSet.Add((x/3) * 1000 + (y/3) * 100000 + val * 31 * 5)) {
                            return false;
                        }
                }
            }
        }

        return true;
    }
}
