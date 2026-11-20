class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # loop through rows

        min_row = set()
        max_col = set()
        for row in range(len(matrix)):
            min_row.add(min(matrix[row]))

        for col in range(len(matrix[0])):
            vals = []
            for row in range(len(matrix)):
                vals.append(matrix[row][col])
            max_col.add(max(vals))

        return list(min_row & max_col)
           


