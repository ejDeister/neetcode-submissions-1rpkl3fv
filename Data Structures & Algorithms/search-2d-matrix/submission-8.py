class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n-1
        while l <= r:
            m = (l+r)//2
            row = m // len(matrix[0])
            col = m - (row*len(matrix[0]))
            v = matrix[row][col]
            if target < v:
                r = m-1
            elif v < target:
                l = m+1
            else:
                return True
            
        return False



        