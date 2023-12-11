class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        heap = []
        for a in nums1:
            heappush(heap, a)
        for b in nums2:
            heappush(heap,b)
        A = [heappop(heap) for i in range(len(heap))]
        if len(A) % 2 == 1:
            return A[len(A)//2]
        else:
            mid = len(A) // 2
            return (A[mid - 1] + A[mid]) / 2.0