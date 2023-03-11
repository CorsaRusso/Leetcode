class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            cur_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, cur_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area