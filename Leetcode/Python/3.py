class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx = st = 0
        seen = dict()
        for i, char in enumerate(s):
            if char in seen and st <= seen[char]:
                st = seen[char] + 1
            else:
                mx = max(mx, i-st+1)
            seen[char] = i
        return mx