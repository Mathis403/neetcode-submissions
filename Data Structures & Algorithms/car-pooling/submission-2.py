from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        bykm = defaultdict(int)

        for t in trips:
            for i in range(t[1], t[2]):
                bykm[i] += t[0]
                if bykm[i] > capacity: 
                    return False
        return True
        