class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        l = 0
        r = len(height) - 1
        maxleft = maxright = 0

        result = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > maxleft:
                    maxleft = height[l]
                else:
                    result += maxleft - height[l]
                l += 1

            else:
                if height[r] > maxright:
                    maxright = height[r]
                else:
                    result += maxright - height[r]
                r -= 1
        return result            
        