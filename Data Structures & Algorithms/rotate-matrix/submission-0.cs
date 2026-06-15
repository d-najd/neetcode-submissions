public class Solution {
    public void Rotate(int[][] matrix) {
        int m = matrix.Length-1;

        for (int x = 0; x < Math.Ceiling((m+1) / 2.0f); x++) {
            for (int y = 0; y < (m+1)/2; y++) {
                int temp = matrix[x][y];

                matrix[x][y] = matrix[m-y][x];
                matrix[m-y][x] = matrix[m-x][m-y];
                matrix[m-x][m-y] = matrix[y][m-x];
                matrix[y][m-x] = temp;
            }
        }
    }
}