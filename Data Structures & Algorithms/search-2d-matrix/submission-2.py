class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n*m - 1


        while l <= r:
            mid = (l+r)//2
            imid = mid//m
            jmid = mid - imid*m


            if matrix[imid][jmid] > target:
                r = mid - 1
            elif matrix[imid][jmid] < target:
                l = mid + 1
            else:
                return True
        return False

        