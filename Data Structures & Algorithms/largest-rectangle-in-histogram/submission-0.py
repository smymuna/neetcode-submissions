class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                area = width * height
                maxArea = max(maxArea, area)
                start = index
            stack.append((start, h))

        n = len(heights)

        while stack:
            index, height = stack.pop()

            width = n - index
            area = width * height
            maxArea = max(maxArea, area)
        
        return maxArea