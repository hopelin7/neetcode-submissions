class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt((x - 0)**2 + (y - 0)**2)
        minHeap = []
        heapq.heapify(minHeap)
        for i in points:
            distance = dist(i[0], i[1])
            heapq.heappush(minHeap, (distance, i))
        

        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
            

        