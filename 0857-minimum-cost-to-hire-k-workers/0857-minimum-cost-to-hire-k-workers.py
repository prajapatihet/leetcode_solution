class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans = math.inf

        sums = 0

        workers = sorted((w/q , q) for q,w in zip(quality,wage))

        maxHeap = []

        for wagePerQuality, q in workers:
            heapq.heappush(maxHeap, -q)

            sums += q

            if len(maxHeap) > k:
                sums += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                ans = min(ans, sums*wagePerQuality)
        
        return ans
