class MinStack:
    
    def __init__(self):
        # Initialize the stack and the min 
        # Have another stack to store the min value
        # At each level track the minimum number and push onto the stack
        self.s = []
        self.minStack = []

    # Push the val element to the top of the stock
    def push(self, val: int) -> None:
        # Keep track of the min every time a value is pushed
        if len(self.minStack) > 0:
            mini = min(self.minStack[-1], val)
            self.minStack.append(mini)
        else:
            self.minStack.append(val)

        self.s.append(val)

    # Pop at the top of the stack 
    # Will always be called on non-empty stacks
    def pop(self) -> None:
        self.s.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
