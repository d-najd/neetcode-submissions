class PrefixTree {
    char: string
    isEnd: boolean
    // Hash map is faster and has less memory
    entries: PrefixTree[] = []

    constructor() {

    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word: string): void {
        if (word.length === 0) return

        const entry = this.entries.find(o => o.char === word[0])
        if (entry) {
            if (word.length === 1) {
                entry.isEnd = true
            }
            entry.insert(word.slice(1, word.length))
        } else {
            const newEntry = new PrefixTree()
            newEntry.char = word[0]
            newEntry.isEnd = word.length === 1
            this.entries.push(newEntry)
            newEntry.insert(word.slice(1))
        }
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word: string): boolean {
        if (word.length === 0 && this.isEnd) return true

        const entry = this.entries.find(o => o.char === word[0])
        if (!entry) { 
            return false
        }

        return entry.search(word.slice(1))
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix: string): boolean {
        if (prefix.length === 0) return true

        const entry = this.entries.find(o => o.char === prefix[0])
        if (!entry) return false
        
        return entry.startsWith(prefix.slice(1))
    }
}
