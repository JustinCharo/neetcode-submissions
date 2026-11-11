class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        numSet = set(nums)
        for num in nums:
            count = 0
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                maxCount = max(length, maxCount)

        return maxCount