class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
    # count the occurence of each letter 
    # store in a hash set with the key being the letter and 
    # the value being the number of times the letter appears
    # letters that do not have the same length is automatically false

        if len(s) != len(t):
            return False

        dict_a = {}
        dict_b = {}

        for char in s:
            if char in dict_a:
                dict_a[char] += 1
            else:
                dict_a[char] = 1
        
        for char in t:
            if char in dict_b:
                dict_b[char] += 1
            else:
                dict_b[char] = 1

        # Compare between the two dictionary to see if all the values match up

        for key in dict_a:
            if dict_b.get(key) is None:
                return False
            else:
                if dict_a.get(key) != dict_b.get(key):
                    return False
        
        return True
