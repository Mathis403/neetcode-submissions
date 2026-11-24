class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])

        res = []

        curInterval = intervals[0]

        for i in range(len(intervals)-1):

            if curInterval[1] < intervals[i+1][0]:
                res.append(curInterval)
                curInterval = intervals[i+1]

            else:
                curInterval = [curInterval[0], max(curInterval[1], intervals[i+1][1])]

        
        res.append(curInterval)

        return res
        