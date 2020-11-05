class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        loop thru prices
        
        if prices[i] < buy:
            update buy
            
        if prices[i] > sell:
            update sell
            
        return max(sell - buy, 0)
        """
        
        max_profit = 0
        
        if len(prices) > 0:
            buy = prices[0]
            sell = prices[0]
            
            for i in range(len(prices)):
                if prices[i] <= buy:
                    buy = prices[i]
                    sell = prices[i]
                    
                if prices[i] > sell:
                    sell = prices[i]
                    if sell - buy > max_profit:
                        max_profit = sell - buy
                    
        return max_profit