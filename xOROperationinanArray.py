class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        array = []
        for i in range(n):
            array.append(start + 2*i)
        for i in range(1,n):
            array[i] = array[i] ^ array[i-1]
        return array[n-1]
