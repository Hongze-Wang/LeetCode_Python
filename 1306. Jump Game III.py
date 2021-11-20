class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)
        if start < 0 or arr[start] < 0 or start >= length:
            return False
        if arr[start] == 0:
            return True
        
        def canReach(arr, start, length):
            queue = []
            queue.insert(0, start)
            
            while len(queue) > 0:
                cur = queue.pop()
                if cur < 0 or cur >= length:
                    return
                if arr[cur] == 0:
                    return True
                if arr[cur] < 0:
                    continue
                
                if cur+arr[cur] < length:
                    queue.insert(0, cur+arr[cur])
                if cur-arr[cur] >= 0:
                    queue.insert(0, cur-arr[cur])
                
                arr[cur] = -arr[cur]
            
            return False
        
        return canReach(arr, start+arr[start], length) or canReach(arr, start-arr[start], length)
