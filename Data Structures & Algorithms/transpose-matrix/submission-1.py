class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        new_m = []
        d = defaultdict(list)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                d[col].append(matrix[row][col])

        for i in range(len(matrix[0])):
            new_m.append(d[i])
        return new_m


            
        
