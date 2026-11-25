class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        stock = -1

        while l <= r:

            mid = (l+r)//2

            nh = 0

            for i in range(len(piles)):

                nh += (piles[i]-1)//mid + 1
            if nh > h:
                l = mid + 1        
            else:
                r = mid - 1
                stock = mid

                
        
        if nh < h:
            return mid
        else:
            return stock


        