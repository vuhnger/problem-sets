from heapq import heappush, heappop
import math

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heappush(heap, (distance, (x,y)))
        res = []
        for i in range(k):
            res.append(heappop(heap)[1])
        return res