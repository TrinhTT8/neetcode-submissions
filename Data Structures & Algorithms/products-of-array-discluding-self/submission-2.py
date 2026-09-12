class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate the prefix product and the postfix product
        # so for at each index
        # we multiply everything to the left of that index
        # we multiple everything to the right of that index
        # the result is the product of these two products

        # have a prefix array
        # have a postfix array
        n = len(nums)
        pref = [1] * n
        post = [1] * n
        res = [1] * n

        # Calculate the prefix list
        for p in range(1, n):
            pref[p] = pref[p-1] * nums[p-1]
        # Calculate the postfix list
        for p in range(n-2, -1, -1):
            post[p] = post[p+1] * nums[p+1]
        
        for r in range(n):
            res[r] = pref[r] * post[r]

        return res
