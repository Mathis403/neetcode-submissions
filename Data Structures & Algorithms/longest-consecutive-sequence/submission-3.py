class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)
        l_max = 0
        i = 0
        if len(nums) <= 1:
            return len(nums)
        while i < len(nums) - 1:
            j = i
            while j < len(nums) - 1 and nums[j+1] - nums[j] == 1:
                j += 1
            l_max = max(l_max, j + 1 - i)
            if i == j:
                j += 1
            i = j
        return l_max
