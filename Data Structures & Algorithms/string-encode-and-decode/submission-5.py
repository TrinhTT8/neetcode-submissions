class Solution:

    # Encode a list of string to a single string
    # Add in the number of characters and a pound sign before each string
    # Ex: 4#neet4#code...
    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + '#' + i
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # Loop through the sentence and separate each word out
        # If read a number follow by a # then we read all the characters
        # after the pound sign up up until the number of characters 
        # match with the number that we read before the #

        while i < len(s):
            j = i
            # j and i are the pointer to the length of each word before #
            # We use two pointers here because the number can be bigger than 1 digit
            while s[j] != "#":
                j += 1
                # string from i to j but not including j
            length = int(s[i:j])
            # we know that # only takes up one space
            # so the start of the word is j + 1
            res.append(s[j + 1 : j + 1 + length])
            # jump i to the start of next word
            i = j + 1 + length
        return res
