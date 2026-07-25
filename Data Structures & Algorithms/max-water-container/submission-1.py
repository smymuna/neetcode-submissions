class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:

            width = right - left
            h = min(heights[left], heights[right])
            area = width * h
            maxArea = max(area, maxArea)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
        
        return maxArea