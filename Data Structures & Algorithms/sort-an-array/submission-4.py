class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] <= l[0]:
                l.insert(0, nums[i])
            elif nums[i] >= l[-1]:
                l.append(nums[i])
            else:
                for j in range(len(l)-1):
                    if l[j]<=nums[i] and l[j+1] >= nums[i]:
                        l.insert(j+1, nums[i])
                        break

        return l

                    