from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event = defaultdict(int)

        for t in trips:
            n, start, end = t
            event[start] += n
            event[end] -= n
        
        s = 0
        for v in sorted(event):
            s += event[v]
            if s > capacity:
                return False
        return True
