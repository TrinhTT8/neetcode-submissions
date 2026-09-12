class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # The numbers are in ascending order
        # Two pointers problem
        # Left pointer and right pointer
        # If the sum of the current numbers are larger than the target
            # We move the right pointer to the left to decrease the sum
        # Else if the sum of the current numbers are smaller than the target
            # We move the left pointer to the right to increase the sum

        l = 0
        r = len(numbers)-1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                print(curr_sum)
                l += 1
            elif curr_sum > target:
                print(curr_sum)
                r -= 1
            else:
                print(curr_sum)
                return [l+1, r+1]