class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # row col pairs
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = []
        steps = 1
        i = 0
        r, c = rStart, cStart
        while len(ans) < rows * cols:
            for _ in range(2):
                dr, dc = directions[i]
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
                    r, c = r + dr, c + dc
                i = (i + 1) % 4
            steps += 1
        return ans

