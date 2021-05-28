class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = []
        seen = {}
        for i in range(len(groupSizes)):
            item = groupSizes[i] #size of group
            if item not in seen: #no room or never seen
                seen[item] = [i]
            else: #there is room to add
                seen[item] += [i]
            if len(seen[item]) == item:
                group.append(seen.pop(item))
        return group
