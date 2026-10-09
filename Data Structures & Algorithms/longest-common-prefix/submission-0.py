class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # For each characters, check if it appears in the other words
        # Start with the first, then add in the second if all of the words have that character and so on
        # But this would give us an O(n^2) since we will be iterating back and forth for each character we add in

        stop_p = False  # Keeps track of when to stop the search
        i = 0
        res = ""
        while i < len(strs[0]):
            for s in range(1, len(strs)):
                if i >= len(strs[s]):
                    return res
                elif strs[0][i] != strs[s][i]:
                    return res
            res += strs[0][i]
            i += 1
                    
        return res

        