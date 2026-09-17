class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Choose two bars to form a container
        # Find the volume within the container
        # Truly you only care about the width of the container and the smallest bar between the two bars

        # Two pointers approach
        l = 0
        r = len(heights)-1
        max_vol = 0

        # We would want the highest bar at all time
        # So if left pointer height < right pointer height
        # We move the left pointer 
        # And then vice versa
        
        while l < r:
            # We determine the volume of the container
            area = min(heights[l],heights[r]) * (r-l)  # r-l gives us the width
            max_vol = max(area, max_vol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_vol