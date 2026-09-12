class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a dictionary to store the key pair values
        temp = {}
        result = list()

        for n in nums:
            if n in temp:
                temp[n] += 1
            else:
                temp[n] = 0
            n += 1
            
        while k != 0:
            max_key = max(temp,key=temp.get)
            result.append(max_key)
            temp.pop(max_key)
            k -= 1
        
        return result

