class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal = 0
        r = 0
        l = 0
        for string in s:
            if string == 'R':
                r +=1
            else:
                l +=1
            if r == l:
                r = 0
                l = 0
                bal +=1
        return bal
