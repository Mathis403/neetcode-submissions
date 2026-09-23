from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        m = -1
        d = defaultdict(int)
        for element in nums:
            d[element] += 1

        print(d)

        for k in d:
            if d[k] == 1:
                m = max(m, k)

        return m