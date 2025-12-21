class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxvol = 0
        while l<r:
            vol = min(height[l], height[r]) * (r-l)
            if vol > maxvol:
                maxvol = vol
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                if height[l+1] >= height[r-1]:
                    l += 1
                else:
                    r -= 1
        return maxvol