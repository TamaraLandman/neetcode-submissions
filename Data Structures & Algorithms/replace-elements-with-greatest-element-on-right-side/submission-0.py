class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        for x in range(len(arr)-1, -1, -1):
            temp = arr[x]
            arr[x] = max_so_far
            max_so_far = max(temp, arr[x])
        return arr
