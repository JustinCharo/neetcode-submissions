class Solution:
    def isValid(self, s: str) -> bool:
        # map with key = opener, value = closed
        stack = []
        bracket_pairs = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in bracket_pairs:
                if stack and stack[-1] == bracket_pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
