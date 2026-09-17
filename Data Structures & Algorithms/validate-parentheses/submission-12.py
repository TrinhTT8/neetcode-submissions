class Solution:
    def isValid(self, s: str) -> bool:

        # We will be using the stack (FILO)
        # We are going to store the open bracket
        # If there is a close bracket that matches with the open bracket
        # We pop the open bracket
        # It is valid if the stack is empty at the end

        brackets = []
        match_map = {')':'(',
                     ']':'[',
                     '}':'{'}

        for c in s:
            if c == '(' or c == '{' or c == '[':
                brackets.append(c)
            elif len(brackets) != 0 and brackets[-1] == match_map[c]:
                brackets.pop()
            else:
                return False

        return not brackets

                