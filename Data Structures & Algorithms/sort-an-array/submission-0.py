class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge sort: divide the array by half and sort each half then merge

        # 1: If the list is empty or has 1 element, it is already sorted
        # 2: If not then split the list into half
        # 3: Sort the left half
        # 4: Sort the right half
        # 5: Merge the two sorted lists into one

        len_list = len(nums)

        if len_list <= 1:
            return nums
        
        mid = len_list//2
        l_half = nums[:mid]
        l_half = self.sortArray(l_half)
        r_half = nums[mid:]
        r_half = self.sortArray(r_half)

        # Do we do the sort here?
        # How do we return the array? 
        def merge(list1, list2):
            l, r = 0, 0
            res = []

            while (l < len(list1) and r < len(list2)):
                if list1[l] <= list2[r]:
                    res.append(list1[l])
                    l += 1
                else:
                    res.append(list2[r])
                    r += 1
                
            # Extend the rest if either pointer hasn't reached the end yet
            res.extend(list1[l:])
            res.extend(list2[r:])
            return res
        
        nums = merge(l_half, r_half)
        return nums    
