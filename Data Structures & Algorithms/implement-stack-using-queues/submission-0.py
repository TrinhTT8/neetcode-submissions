class MyStack:

    def __init__(self):
        self.q = deque()

    # To have the queue behaves like a stack, we need to rotate the most recent added element to the front 
    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # just pop from the front since we already rotated the queue
        return self.q.popleft()

    # Queue peeks from the front so we need to move the elements again?
    def top(self) -> int:
        if len(self.q) == 0:
            return None
        
        return self.q[0]

    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()