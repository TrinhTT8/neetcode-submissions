class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use bucket sort and the number of buckets would be the total amount of number in the list
        # Each index will represent the frequency of a number
        # Each value will be a list of all the number that appears that amount of time
        # We can use hash map to count the value

        num_freq = {}
        # Initialize the bucket from 1 to max len of nums
        # remember range goes from 0 to 
        bucket_s = [[] for i in range (len(nums) + 1)]

        for i in nums:
            if i in num_freq:
                num_freq[i] += 1
            else:
                num_freq[i] = 1
        
        for key in num_freq:
            # Put the number to the corresponding frequency in the bucket
            bucket_s[num_freq[key]].append(key)
        
        res = []
        for i in range(len(bucket_s) - 1, 0, -1):
            # Loop through the list value within the bucket
            for num in bucket_s[i]:
                res.append(num)
                if len(res) == k:
                    return res
