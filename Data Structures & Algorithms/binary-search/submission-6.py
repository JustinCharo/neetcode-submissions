class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [-1, 0, 2, 4, 6, 8], target = 4
        left = 0 -> -1
        right = 5 -> 8
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1