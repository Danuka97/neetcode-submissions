class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) -1
        max_ara = 0

        while l <r:
            h =  min(heights[l],heights[r])
            w = r - l 

            area = h * w
            max_ara = max(max_ara,area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_ara
        