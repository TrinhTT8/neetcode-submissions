#Bucket sort solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We need a hash map to keep the occurence of each number
        count = {}
        # Initialize the bucket to the size of the array, which is just dict
        bucket = [[] for i in range(len(nums) + 1)]

        for i in nums:
            # count.get(i, 0) check for the value at key i
            # if no value found then return 0
            count[i] = 1 + count.get(i, 0)

        # Now we go through each number and its occurence to add to the list
        for i, c in count.items():
            # count is our index in the list
            bucket[c].append(i)

        top = []
        # Iterate through the list from the end
        # We store from smallest to highest occurence within the list
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                top.append(n)
                if len(top) == k:
                    return top
