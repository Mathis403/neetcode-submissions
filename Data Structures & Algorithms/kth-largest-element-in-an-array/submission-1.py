import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lk = nums[:k]

        heapq.heapify(lk)

        for i in range(k, len(nums)):
            if nums[i] > lk[0]:
                heapq.heapreplace(lk, nums[i])
        return lk[0]        

