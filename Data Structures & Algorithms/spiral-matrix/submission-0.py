class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # create 4 boundaries
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        while left < right and top < bottom:
            # copies the first row
            for i in range(left, right):
                res.append(matrix[top][i])
            # increment top bc we are done with the top row
            top += 1
            # traverse the right side
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            # check if matrix is invalid
            if not (left < right and top < bottom):
                break

            # traverse the bottom
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # traverse the left side
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
                
            left += 1

        return res


        