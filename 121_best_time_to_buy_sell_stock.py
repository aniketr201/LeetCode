class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        leftPointer = 0
        rightPointer = 1
        while rightPointer < len(prices):
            if prices[leftPointer] < prices[rightPointer]:
                profit = prices[rightPointer] - prices[leftPointer]
                if profit > maxProfit:
                    maxProfit = profit
                rightPointer += 1
            else:
                leftPointer = rightPointer
                rightPointer = leftPointer + 1
        return maxProfit
