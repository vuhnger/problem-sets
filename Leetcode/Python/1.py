class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numToIdx = dict()
        for i, num in enumerate(nums):
            if target - num in numToIdx:
                return [numToIdx[target - num], i]
            numToIdx[num] = i
        return []