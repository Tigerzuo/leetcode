class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        index = range(0,len(nums),2)
        final = []
        for i in index:
            val = nums[i+1]
            for j in range(nums[i]):
                final.append(val)
        return final
