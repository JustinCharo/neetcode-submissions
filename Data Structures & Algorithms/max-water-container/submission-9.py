class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # for 2 bars, the height is defined by the smaller height
        # width is just the distance from r to l?
        # update area by doing j - i * (min(height(i), height(j))
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            max_area = max(area, max_area)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return max_area


