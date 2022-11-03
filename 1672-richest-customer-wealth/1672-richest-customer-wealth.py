class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        list_wealth_per_customer = [sum(account) for account in accounts]
        max_wealth_customer = max(list_wealth_per_customer)
        
        return max_wealth_customer