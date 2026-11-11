class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate (nums):
            diff = target - num
            if diff in complements:
                return [complements[diff], i]
            complements[num] = i

        return False
