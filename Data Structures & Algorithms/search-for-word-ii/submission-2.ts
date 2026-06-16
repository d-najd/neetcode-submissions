class Solution {
    result: string[] = []
    /**
     * @param {character[][]} board
     * @param {string[]} words
     * @return {string[]}
     */
    findWords(board: string[][], words: string[]): string[] {
        for (var y = 0; y < board.length; y++) {
            for (var x = 0; x < board[0].length; x++) {
                for (var w = 0; w < words.length; w++) {
                    this.findWord(board, words[w], x, y, [])
                }
            }
        }

        return this.result
    }

   findWord(board: string[][], word: string, x: number, y: number, checked: number[][]) {
        if (board[y][x] !== word[checked.length]) return 
        if (checked.some(([xc, yc]) => xc === x && yc === y)) return

        const newChecked = [...checked]
        newChecked.push([x, y])
        if (word.length === newChecked.length) {
            this.result.push(word)
            return
        }

        this.findWord(board, word, Math.min(board.length - 1, x+1), y, newChecked)
        this.findWord(board, word, Math.max(x-1, 0), y, newChecked)
        this.findWord(board, word, x, Math.min(board.length - 1, y+1), newChecked)
        this.findWord(board, word, x, Math.max(y-1, 0), newChecked)
   }
}
