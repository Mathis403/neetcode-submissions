class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        mn = min(nums[0], 0)
        mx = nums[0]

        s = nums[0]

        res = s

        for i in range(1, len(nums)):

            if s + nums[i] > mx:
                s += nums[i]
                mx = s
                res = max(mx - mn, res)

            elif nums[i] <= 0 and nums[i] > res:
                res = nums[i]

            elif s + nums[i] < mn:
                s = 0
                mn = 0
                mx = 0

            
            else:
                s += nums[i]

        return res
            
        