class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows*cols-1
        while l <= r:
            m = math.floor((l+r)/2)
            row = math.floor(m/cols)
            col = m - (row*cols)
            v = matrix[row][col]
            if target < v:
                r = m-1
            elif v < target:
                l = m+1
            else:
                return True
            
        return False



        