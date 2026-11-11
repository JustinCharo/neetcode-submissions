class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        # disregard all negative numbers if not positive
        currSum = 0
        for i in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += i

            if currSum > maxSum:
                maxSum = currSum
            
        return maxSum