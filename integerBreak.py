class Solution:
    def integerBreak(self, n: int) -> int:
        num3 = 0
        num2 = 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        while n>0:
            if n==3:
                n=0
                num3+=1
            elif n==4:
                num2+=2
                n -=4
            elif n==2:
                num2+=1
                n-=2
            else:
                num3+=1
                n-=3
        return 2**num2 * 3**num3
