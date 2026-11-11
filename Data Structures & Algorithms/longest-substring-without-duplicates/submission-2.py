class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Need to track all characters included so far
        # zxyzxyzabcdea
        l = 0
        sub_set = set()
        max_length = 0
        for r in range (len(s)):
            while s[r] in sub_set:
                sub_set.remove(s[l])
                l += 1
            sub_set.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length
