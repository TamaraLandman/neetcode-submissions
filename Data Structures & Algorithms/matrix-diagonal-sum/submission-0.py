class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        ans = 0
        n = len(mat)
        col = len(mat[0])-1

        for row in range(len(mat)):
            ans += mat[row][row]
            ans += mat[row][col-row]

        if n % 2 == 1:
            ans = ans - mat[n//2][n//2]
        return ans
        