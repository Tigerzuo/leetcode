class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        final = [first]
        for i in range(len(encoded)):
            final.append(final[i]^encoded[i])
            
        return final
