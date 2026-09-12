class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point1 = 0
        point2 = len(numbers)-1
        total = 0

        while point1 != point2:
            total = numbers[point1] + numbers[point2]
            if total == target:
                break
            elif total > target:
                point2 -= 1
            else:
                point1 += 1
        
        return [point1+1, point2+1]
