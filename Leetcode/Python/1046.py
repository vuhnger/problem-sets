class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        from heapq import heapify, heappop, heappush
        heap = [-x for x in stones]
        while len(heap) > 1:
            heapify(heap)
            a = heappop(heap)
            b = heappop(heap)
            heappush(heap, -abs(a-b))
        return abs(heap[0])