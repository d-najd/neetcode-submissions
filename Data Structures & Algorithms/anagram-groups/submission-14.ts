class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        var result: string[][] = []

        for (var l = 0; l < strs.length; l++) {
            var lStr = strs[l]
            if (lStr === '0') continue

            result.push([lStr])
            for (var r = l+1; r < strs.length; r++) {
                var rStr = strs[r]

                if (rStr === '0' || lStr.length !== rStr.length) {
                    continue
                }
                
                const map = new Map<string, number>();
                for (var lc of lStr) {
                    var count = map.get(lc) ?? 0
                    count++
                    map.set(lc, (map.get(lc) ?? 0)+1)
                }

                for (var rc of rStr) {
                    var count = map.get(rc)
                    if (!count) break 
                    if (count === 1) {
                        map.delete(rc)
                    } else {
                        map.set(rc, count - 1)
                    }
                }

                // Match
                if (map.size === 0) {
                    strs[r] = '0'
                    result[result.length - 1].push(rStr)
                }
            }
        }

        return result
    }
}
