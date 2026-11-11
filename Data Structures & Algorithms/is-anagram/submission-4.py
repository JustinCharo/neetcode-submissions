class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        for char in s:
            s_count[char] = 1 + s_count.get(char, 0)

        t_count = {}
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)

        return s_count == t_count
        