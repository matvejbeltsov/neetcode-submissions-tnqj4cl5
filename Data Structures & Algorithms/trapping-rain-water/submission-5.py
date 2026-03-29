class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxleft = maxright = 0

        max_water = 0 

        while l < r:

            if height[l] < height[r]:
                if height[l] > maxleft:
                    maxleft = height[l]
                else:
                    max_water += maxleft - height[l]
                l += 1
            else:
                if height[r] > maxright:
                    maxright = height[r]
                else:
                    max_water += maxright - height[r]
                r -= 1
        return max_water
        