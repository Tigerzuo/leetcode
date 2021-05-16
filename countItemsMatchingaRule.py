class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for typ,color,name in items:
            if ruleKey == "type" and ruleValue == typ:
                count += 1
            elif ruleKey == "color" and ruleValue == color:
                count += 1
            elif ruleKey == "name" and ruleValue == name:
                count += 1
            else:
                continue
        return count
