class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = abs(heapq.heappop(heap))
            x = abs(heapq.heappop(heap))
            if x < y:
                y = y - x
                heapq.heappush(heap, y * -1)
        
        return abs(heapq.heappop(heap)) if heap else 0

        