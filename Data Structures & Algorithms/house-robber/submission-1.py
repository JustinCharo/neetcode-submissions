class Solution:
    def rob(self, nums: List[int]) -> int:
        robi, robj = 0, 0

        for num in nums:
            temp = max(num + robi, robj)
            robi = robj
            robj = temp

        return robj
        
