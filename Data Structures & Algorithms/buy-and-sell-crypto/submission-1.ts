class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let mostProfitableTransaction = 0
        let smallestLeftIndex = 0
        
        for (var i = 1; i < prices.length; i++) {
            if (prices[smallestLeftIndex] > prices[i]) {
                smallestLeftIndex = i
            } else {
                mostProfitableTransaction = Math.max(prices[i] - prices[smallestLeftIndex], mostProfitableTransaction)
            }
        }

        return mostProfitableTransaction
    }
}
