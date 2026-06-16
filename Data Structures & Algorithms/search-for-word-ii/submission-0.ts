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
                const initialChar = board[y][x]
                for (var w = 0; w < words.length; w++) {
                    //if (initialChar === words[w][0]) {
                        this.findWord(board, words[w], x, y, [])
                    //}
                }
            }
        }

        return this.result
    }

   findWord(board: string[][], word: string, x: number, y: number, checked: number[][]) {
        //if (this.result.length !== 0 && this.result[this.result.length - 1] === word) return
        //console.log(`PW ${word} ${x} ${y}: ${checked}`)
        if (board[y][x] !== word[checked.length]) return 
        if (checked.some(([xc, yc]) => xc === x && yc === y)) return
        //console.log(`PW ${word} ${x} ${y}: ${checked}`)
        //console.log(`L ${word.length} C ${checked.length}`)
        checked.push([x, y])
        if (word.length === checked.length) {
            //console.log("PUSHING")
            this.result.push(word)
            return
        }

        this.findWord(board, word, Math.min(board.length - 1, x+1), y, [...checked])
        this.findWord(board, word, Math.max(x-1, 0), y, [...checked])
        this.findWord(board, word, x, Math.min(board.length - 1, y+1), [...checked])
        this.findWord(board, word, x, Math.max(y-1, 0), [...checked])
   }
}
