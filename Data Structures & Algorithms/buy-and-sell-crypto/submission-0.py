class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        for i in range(1,len(prices)):
            new = max(prices[i:len(prices)])-min(prices[0:i])
            if new>profit:
                profit = new
        return profit