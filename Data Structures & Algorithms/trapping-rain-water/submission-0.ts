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

        var trappedCount = 0
        for (var y = maxHeight; y >= 0; y--) {
            var hitWall = false
            var maybeTrappedCount = 0

            var index = 0
            for (var x of height) {

                //console.log(`Checking ${y} ${index} ${x} ${trappedCount}`)
                index++
                if (x >= y) {
                    if (!hitWall) {
                        //console.log(`Hitting wall`)
                        hitWall = true
                    } else {
                        //console.log(`Hitting wall another time`)
                        trappedCount += maybeTrappedCount
                        maybeTrappedCount = 0
                    }
                } else {
                    if (hitWall) {
                        //console.log(`Incrementing`)
                        maybeTrappedCount++
                    }
                }
            }
        }

        return trappedCount
    }
}
