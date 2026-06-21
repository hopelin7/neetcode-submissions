class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        print(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop_max(maxHeap)
            y = heapq.heappop_max(maxHeap)

            if x < y:
                heappq.heappush_max(maxHeap, y - x)
            if y < x:
                heapq.heappush_max(maxHeap, x - y)
        return maxHeap[0] if len(maxHeap) == 1 else 0




        
