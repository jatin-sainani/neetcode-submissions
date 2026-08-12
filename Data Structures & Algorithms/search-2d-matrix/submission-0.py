class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        # print(m,n)

        

        top, bottom = 0, m

        while top<=bottom:
            midrow = int((top + bottom)/2)
            if target>=matrix[midrow][0] and target<=matrix[midrow][n]:
                print('correct row:', midrow)
                break
            elif target>matrix[midrow][n]:
                top = midrow + 1
            elif target<matrix[midrow][0]:
                bottom = midrow - 1
        
        
        l,r = 0 , n
        while l<=r:
            midcol = int((l+r)/2)
        #check that row
            if target == matrix[midrow][midcol]:
                return True
            elif target < matrix[midrow][midcol]:
                r = midcol - 1
            elif target > matrix[midrow][midcol]:
                l = midcol + 1
        return False

        