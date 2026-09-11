class Solution:
    def findMin(self, nums: List[int]) -> int:
        def min(l):

            if len(l) == 1:
                return l[0]
            if len(l) == 2:
                return l[0] if l[0] < l[1] else l[1]
            if len(l)%2 == 0:
                l1 = l[:len(l)//2]
                l2 = l[len(l)//2:]
            else:
                l1 = l[:len(l)//2]
                l2 = l[len(l)//2:]
            
            if ((l1[0]<=l1[-1])and(l1[0]>l2[-1])):
                m = min(l2)
            else:
                m = min(l1)
            return m
        return min(nums)