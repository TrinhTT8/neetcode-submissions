class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Use a hash map to store the complementary
        # Ex: If the target is 8 and the list is [1,2,3,4,5]
        # 8-1 = 7 (we store it in the hash map)
        # We find the two sum by finding the complementary number within the list
    
        # key = the number at index i
        # value = i
        comp_dict= {}

        for i in range(len(nums)):
            c = target - nums[i]

            # Check if the complement exists
            if c in comp_dict:
                return [comp_dict[c], i]
            
            # If not then we add it to the hash map
            comp_dict[nums[i]] = i
        
            