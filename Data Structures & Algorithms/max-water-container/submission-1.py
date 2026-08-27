class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left = 0
        right = len(heights) - 1

        while right > left :
            if heights[left] > heights[right] :
                area = heights[right] * (right - left)
                res = max(res, area)
                right -= 1
                continue
            
            elif heights[left] <= heights[right] :
                area = heights[left] * (right - left)
                res = max(res, area)
                left += 1
                continue

            """else:
                area = heights[left] * (right - left)
                res = max(res, area)
                left += 1
                continue"""

        return res

