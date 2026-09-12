class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point1 = 0
        point2 = len(numbers)-1
        total = 0

        # Stop the loop if the two pointer meets
        while point1 != point2:
            total = numbers[point1] + numbers[point2]
            if total == target:
                break
            # If the total is larger than the target, we move the right pointer to the left
            elif total > target:
                point2 -= 1
            # If the total is smaller than the target, we move the left pointer to the right
            else:
                point1 += 1
        
        return [point1+1, point2+1]
