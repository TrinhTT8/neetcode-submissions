class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        # Count the number of occurence of each letter in a string
        for i in strs:
            # 26 letters in the alphabelt
            count = [0] * 26
            # Use ASCII value to place the letter to its corresponding index
            for s in i:
                count[ord(s) - ord('a')] += 1
            
            # REMEMBER: A list cannot be a stored as a key
            # Have to convert to tuple because it is immutable
            result[tuple(count)].append(i)

        return list(result.values())


        