class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(index)):
            j = index[i]
            num = nums[i]
            target.insert(j,num)
        return target
