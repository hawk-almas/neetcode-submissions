class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0


        for i in prices:
            if minPrice < i :
                res = max(res, i - minPrice)
            else:
                minPrice = i

        return res
