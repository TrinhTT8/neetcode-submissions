class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search
        # Find mid point and evaluate whether to drop the left or right array
        # We need to find which side is the sorted first
        # Check if the target is within that range of the sorted side
        # If not then we perform the search in the unsorted side
        
        l, r = 0, len(nums)-1
       
        # Use <= because there might be time where the list only has 1 value [2]
        while l <= r:
            mid = (l+r) // 2
            # return mid if the target is at mid
            if target == nums[mid]:
                return mid
            
            # Left side is sorted if this is true
            elif nums[mid] >= nums[l]:
                # If target is larger than or equal to the left most value
                # and smaller than the mid value then we know it is in this range
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1     # We rule out that mid is not it 
                else:
                # If not then we search the unsorted side (right)
                    l = mid + 1
            # Right is sorted
            else:
                # Check if the target is within the right side
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                # If not then we search the unsorted side (left)
                else:
                    r = mid - 1


        return -1