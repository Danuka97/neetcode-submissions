class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = len(heights) -1
        right = 0
        best = 0

        while left > right:

            L = left - right
            A = L * min(heights[right],heights[left])
            best = max(best,A)
            if heights[right] > heights[left]:
                left = left - 1
            else:
                right = right +1
        return best






        