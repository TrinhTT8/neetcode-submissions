class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # To be an anagram, two strings must have equal length
        if len(s) != len(t):
            return False
        
        # Use a hash map to store the how many time a character appears in the string
        # Then check to see if all the values match at the end
        dict_a = {}
        dict_b = {}
        
        for i in s:
            if i in dict_a:
                dict_a[i] += 1
            else:
                dict_a[i] = 1

        for i in t:
            if i in dict_b:
                dict_b[i] += 1
            else:
                dict_b[i] = 1
        
        # Check between the two dictionary using key of dict_a
        for key in dict_a:
            if dict_b.get(key) == None:
                return False
            # If the value of one of the character doesn't match, we return False
            else:
                if dict_a.get(key) != dict_b.get(key):
                    return False
        
        return True