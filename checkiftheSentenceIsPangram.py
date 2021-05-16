class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        myset = set()
        for i in sentence:
            myset.add(i)
        return len(myset) == 26
