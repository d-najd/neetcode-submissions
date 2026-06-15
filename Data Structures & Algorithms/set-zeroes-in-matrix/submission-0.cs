public class Solution {
    public void SetZeroes(int[][] matrix) {
        List<Tuple<int, int>> list = new();
        for (int x = 0; x < matrix[0].Length; x++) {
            for (int y = 0; y < matrix.Length; y++) {
                if (matrix[y][x] == 0) {
                    list.Add(new (x, y));
                }
            }
        }

        for (int i = 0; i < list.Count; i++) {
            var cur = list[i];
            for (int x = 0; x < matrix[0].Length; x++) {
                matrix[cur.Item2][x] = 0;            
            }

            for (int y = 0; y < matrix.Length; y++) {
                matrix[y][cur.Item1] = 0;
            }
        } 
    }
}