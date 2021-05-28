class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        forward = 0
        current = 0
        backward = 0
        first = 0 #distance for first element
        
        if boxes[0] == '1':
            current = 1
            
        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                forward += 1
                first += i
                
        answer.append(first)
        
        for i in range(len(boxes)-1):
            diff = - forward + current + backward
            answer.append(answer[i]+diff)
            try:
                if current == 1:
                    current = 0
                    backward += 1
                if boxes[i+1] == '1':
                    forward -= 1
                    current = 1
            finally:
                continue
                
        return answer
