public class Solution {
    public void SetZeroes(int[][] matrix) {
        bool xC = false;
        bool yC = false;

        for (int x = 0; x < matrix[0].Length; x++) {
            if (matrix[0][x] == 0) {
                xC = true;
            }
          
        }
        for (int y = 0; y < matrix.Length; y++) {
            if (matrix[y][0] == 0) {
                yC = true;
            }
        }

        for (int x = 1; x < matrix[0].Length; x++) {
            for (int y = 1; y < matrix.Length; y++) {
                if (matrix[y][x] == 0) {
                    matrix[y][0] = 0;
                    matrix[0][x] = 0;
                }

                if (matrix[y][0] == 0 || matrix[0][x] == 0) {
                    matrix[y][x] = 0;
                }
            }
        }

        if (xC) {
            for (int x = 0; x < matrix[0].Length; x++) {
                matrix[0][x] = 0;
            }
        }
        if (yC) {
            for (int y = 0; y < matrix.Length; y++) {
                matrix[y][0] = 0;
            }
        }
        
    }
}