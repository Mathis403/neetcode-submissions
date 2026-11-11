class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = []

        for num in nums:
            for j in range(len(l)):
                if num <= l[j]:
                    l.insert(j, num)
                    break
            else:
                l.append(num)

        return l