from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for e in nums:
            d[e] += 1

        l = sorted(list(d.keys()), key = lambda x : d[x], reverse = True)
        


        
        return l[:k]
        
        