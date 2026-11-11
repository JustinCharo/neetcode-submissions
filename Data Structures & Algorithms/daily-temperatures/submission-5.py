class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # tuple, (temp, index)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_idx = stack.pop()
                result[stack_idx] = i - stack_idx
            stack.append((temp, i))
        return result