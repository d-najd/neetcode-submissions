class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height: number[]): number {
        var maxHeight = 0
        for (var cur of height) {
            if (cur > maxHeight) {
                maxHeight = cur
            }
        }

        const heightArray = new Array(maxHeight + 1).fill(-1);

        var trappedCount = 0
        for (var x = 0; x < height.length; x++) {
            const cur = height[x]
            if (cur === 0) continue

            for (var y = cur - 1; y >= 0; y--) {
                if (heightArray[y] !== -1) {
                    const addCo = (x - 1) - heightArray[y]
                    trappedCount += addCo
                } 
                heightArray[y] = x
            }
        }
        return trappedCount
        /*
        for (var y = maxHeight; y >= 0; y--) {
            var hitWall = false
            var maybeTrappedCount = 0

            var index = 0
            for (var x of height) {
                index++
                if (x >= y) {
                    if (!hitWall) {
                        hitWall = true
                    } else {
                        trappedCount += maybeTrappedCount
                        maybeTrappedCount = 0
                    }
                } else {
                    if (hitWall) {
                        maybeTrappedCount++
                    }
                }
            }
        }
        */

        return trappedCount
    }
}
