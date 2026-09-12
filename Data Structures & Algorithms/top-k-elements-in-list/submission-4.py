class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build a list of list of frequency 
        # Where index represents the frequency and the list stores the number with the corresponding frequency

        result = []
        # The maximum possible frequency is the length of the array
        freq=[[] for i in range(len(nums)+1)]

        # Count the numbers and put the frequency in a hash map
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        # Then we put all the numbers based on the frequency which is the index to the list
        for num in count:
            freq[count[num]].append(num)

        # Loop from the highest index to get the largest possible frequency number
        for i in range(len(freq) - 1, 0, -1):
            # Loop through each number in the inner list
            for n in freq[i]:
                # If the len of the result list is less than k then we keep adding
                if len(result) == k:
                    break
                result.append(n)
        
        return result