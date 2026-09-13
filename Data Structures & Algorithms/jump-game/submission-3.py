from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        @cache
        def canJumpRec(i):
            if i == len(nums) - 1:
                return True

            if nums[i] == 0:
                return False

            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if canJumpRec(j):
                    return True

            return False

        return canJumpRec(0)