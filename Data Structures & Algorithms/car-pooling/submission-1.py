class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        bykm = {}

        for t in trips:
            for i in range(t[1], t[2]):
                if i not in bykm.keys():
                    bykm[i] = t[0]
                else:
                    bykm[i] += t[0]
                if bykm[i] >capacity: 
                    return False
        return True
        