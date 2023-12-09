from heapq import heappush, heappop, heapify
import math

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = [(x**2 + y**2, (x,y)) for x,y in points]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]