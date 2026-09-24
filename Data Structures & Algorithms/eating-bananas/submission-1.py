class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Use binary search to find the minimum rate value
        # Use ceil(pile/rate) to find the total hours to eat that pile
        # Find the final hours and compare it with h
        # If the final hours is smaller than h then we search left
        # If it is larger than we search right

        # No need to create a list here 
        # Just use l and r to represent the rates 
        # and narrow it down by binary search
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l+r)//2
            total_hr = 0
            for i in piles:
                total_hr += math.ceil(float(i)/mid)
            if total_hr <= h:
                res = mid
                r = mid - 1
            else:   # Search right
                l = mid + 1
        
        return res
