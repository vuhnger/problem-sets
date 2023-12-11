class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = defaultdict(lambda: 0)
        one_fourth = len(arr) >> 2
        for i in arr:
            freq[i] +=1
            if freq[i] > one_fourth:
                return i
        return -1