class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const numsMap = new Map<number, number>()
        for (var num of nums) {
            numsMap.set(num, (numsMap.get(num) ?? 0) + 1)
        }

        const result = [...numsMap.entries()].sort(([fk, fv], [sk, sv]) => sv - fv).filter((v, i) => {            
            if (i >= k) return false
            return true
        }).map((k, v) => k[0])

        return result
    }
}
