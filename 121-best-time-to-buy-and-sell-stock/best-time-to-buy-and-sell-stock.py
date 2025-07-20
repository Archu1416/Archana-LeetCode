class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=prices[0]
        max_=0
        for i in prices[1:]:
            profit=i-min_
            if profit>max_:
                max_=profit
            if i<min_:
                min_=i
        return max_