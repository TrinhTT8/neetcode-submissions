class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

       # Loop through the array, scanning for each number
       # For each number, we will store the number in a set
       # Python uses a hash map for set so the lookup time is O(1)
       # If a number is already in a set, then we halt the program and return that number
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                break

        return i