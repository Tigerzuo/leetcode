class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer=[]
        for circle in queries:
            r = circle[2]
            inside = 0
            for point in points:
                dist = sqrt((point[0]-circle[0])**2 + (point[1]-circle[1])**2)
                if r >= dist:
                    inside += 1
            answer.append(inside)
        return answer
