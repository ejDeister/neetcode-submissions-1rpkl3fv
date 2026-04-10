class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def val(matrix: List[List[int]], i: int) -> List[int]:
            row = i // len(matrix[0])
            col = i - (row*len(matrix[0]))
            print('val',i,row,col)
            return matrix[row][col]

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n-1
        while l <= r:
            m = (l+r)//2
            v = val(matrix, m)
            print(l,r,m,v)
            if target < v:
                r = m-1
            elif v < target:
                l = m+1
            else:
                return True
            
        return False



        