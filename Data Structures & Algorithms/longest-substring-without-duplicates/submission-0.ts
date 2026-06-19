class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        var maxLen = 0
        const cs = []

        for (var i = 0; i < s.length; i++) {
            const c = s[i]
            if (cs.includes(c)) {
                // Shift until element is removed
                while (cs.shift() !== c) { }
            }

            cs.push(c)
            if (cs.length > maxLen) {
                maxLen = cs.length
            }
        }

        return maxLen
    }
}
