class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0

        for i in range(len(heights) + 1):
            currentHeight = 0 if i == len(heights) else heights[i]

            while stack and currentHeight < heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = h * width
                maxArea = max(maxArea, area)

            stack.append(i)

        return maxArea