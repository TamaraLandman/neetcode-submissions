class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for c in range(n)] for r in range(n)]
        
        num = 1
        left, right = 0, n
        top, bottom = 0, n

        while left < right and top < bottom:
            # copy top
            for i in range(left, right):
                matrix[top][i] = num
                num += 1
            top += 1

            # copy right

            for i in range(top, bottom):
                matrix[i][right-1] = num
                num += 1
            right -= 1

            if not( left < right and top < bottom):
                break
            
            # traverse bottom
            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = num
                num += 1
            bottom -= 1 
            # traverse left
            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix