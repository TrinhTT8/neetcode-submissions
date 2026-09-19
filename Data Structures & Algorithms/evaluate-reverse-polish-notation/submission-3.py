class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # We push all the elements into a stack
        # Stack is FILO
        # Operations that are being pushed first are the most important 
        # Since they belong to the inside of the calculation
        # Only take two operands at a time
        temp_stack = []

        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                temp_stack.append(int(i))
            else:
                # Pop 2 operands each time 
                o1 = temp_stack[-1]
                temp_stack.pop()
                o2 = temp_stack[-1]
                temp_stack.pop()
                if i == '+':
                    temp_stack.append(o2 + o1)
                elif i == '-':
                    temp_stack.append(o2 - o1)
                elif i == '*':
                    temp_stack.append(o2 * o1)
                elif i == '/':
                    temp_stack.append(int(o2 / o1))

        return temp_stack[-1]
