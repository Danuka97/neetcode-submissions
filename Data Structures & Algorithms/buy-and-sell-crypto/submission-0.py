class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r=1
        max_pro = 0 
        
        while r < len(prices):

            if prices[r] > prices[l]:
                
                pro = prices[r] - prices[l]

                max_pro = max(max_pro,pro)

            else:
                l = r
            
            r += 1
        return max_pro

