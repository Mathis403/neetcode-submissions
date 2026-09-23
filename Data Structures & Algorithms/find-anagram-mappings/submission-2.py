from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        d1 = defaultdict(list)
        d2 = defaultdict(list)

        for i, num in enumerate(nums1):
            d1[num].append(i)

        for i, num in enumerate(nums2):
            d2[num].append(i)

        
        for k in d1.keys():
            for i in range(len(d1[k])):
                res[d1[k][i]] = d2[k][i]
        return res

            

        