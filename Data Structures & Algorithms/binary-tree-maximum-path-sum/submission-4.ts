/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

/*
       5
    4     8
  11 n  13  4
 7  2 nnn 1
*/ 
// 27 + 8 35 13 48
class Solution {
    biggest = -999999

    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxPathSum(root: TreeNode | null): number {
        let newSum = root.val
        const leftSum = this.maxPathSumInternal(root.left)
        const rightSum = this.maxPathSumInternal(root.right)

        // console.log(leftSum + " " + rightSum)

        if (leftSum > 0) {
            newSum += leftSum
        }

        if (rightSum > 0) {
            newSum += rightSum
        }

        if (newSum > this.biggest) {
            this.biggest = newSum
        }
        
        return this.biggest
    }

    maxPathSumInternal(root: TreeNode | null) {
        if (root === null) return 0

        const leftSum = this.maxPathSumInternal(root.left)
        const rightSum = this.maxPathSumInternal(root.right)

        let newSum = root.val
        if (leftSum > 0) {
            newSum += leftSum
        }

        if (rightSum > 0) {
            newSum += rightSum
        }

        if (newSum > this.biggest) {
            this.biggest = newSum
        }

        const newSumNonBoth = root.val + Math.max(Math.max(leftSum, rightSum), 0)
        if (newSumNonBoth > this.biggest) {
            this.biggest = newSumNonBoth
        }
        // console.log(`NODE ${root.val} SUM ${newSum} NOD ${newSumNonBoth} LEF ${leftSum} RIG ${rightSum}`)

        return newSumNonBoth
    }
}
