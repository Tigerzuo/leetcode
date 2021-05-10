class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for person in accounts:
            personal_wealth = 0
            for bank in person:
                personal_wealth += bank
            if personal_wealth > wealth:
                wealth = personal_wealth
                
        return wealth
