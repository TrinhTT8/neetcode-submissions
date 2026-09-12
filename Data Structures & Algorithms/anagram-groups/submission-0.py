class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Use a hash map to map charCount to a list of Anagrams
        res = defaultdict(list)

        for s in strs:
            # Create an array for 26 letters (a....z)
            count = [0]*26
            # Go through every character in each string and count how many characters
            for c in s:
                # store a at 0 index, and z at the 25 index
                # use ASCII value (ord(n))
                count[ord(c) - ord('a')] += 1

            # List is mutable so it cannot be a key value
            # You need to append to the list anyway so if-else statement is not really needed
            res[tuple(count)].append(s)

        return list(res.values())