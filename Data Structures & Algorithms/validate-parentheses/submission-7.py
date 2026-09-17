class Solution:
    def isValid(self, s: str) -> bool:

        # We will be using the stack (FILO)
        # We are going to store the open bracket
        # If there is a close bracket that matches with the open bracket
        # We pop the open bracket
        # It is valid if the stack is empty at the end

        brackets = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                brackets.append(c)
            elif c == ')':
                if len(brackets) == 0 or brackets[-1] != '(':
                    return False
                elif brackets[-1] == '(':
                    brackets.pop()
            elif c == '}':
                if len(brackets) == 0 or brackets[-1] != '{':
                    return False
                elif brackets[-1] == '{':
                    brackets.pop()
            elif c == ']':
                if len(brackets) == 0 or brackets[-1] != '[':
                    return False
                elif brackets[-1] == '[':
                    brackets.pop()

        if len(brackets) == 0:
            return True
        else:
            return False

                