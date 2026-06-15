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

class Solution {
    biggest = -999999

    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxPathSum(root: TreeNode | null): number {
        this.maxPathSumInternal(root)
        
        return this.biggest
    }

    maxPathSumInternal(root: TreeNode | null) {
        if (root === null) return 0

        const leftSum = this.maxPathSumInternal(root.left)
        const rightSum = this.maxPathSumInternal(root.right)

        let newSum = root.val

        newSum += Math.max(leftSum, 0)
        newSum += Math.max(rightSum, 0)
    
        if (newSum > this.biggest) {
            this.biggest = newSum
        }

        const newSumNonBoth = root.val + Math.max(Math.max(leftSum, rightSum), 0)
        return newSumNonBoth
    }
}
