class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # initialize a stack of len(temperatures) filled with 0
    # Go through the list:
        # If the temp[i] > stack.peek(), we pop the stack
        # We continue to check the next peek until temp[i] < stack.peek() or stack is empty
        # Then we push in "i"
        # Else if temp[i] < stack.peek(), we push the "i"
        # Calculate the index by i - value at peek

        res = [0] * len(temperatures)
        s_temp = []
        for i in range(len(temperatures)):
            if s_temp and temperatures[i] > temperatures[s_temp[-1]]:
                while s_temp and temperatures[i] > temperatures[s_temp[-1]]:
                    res[s_temp[-1]] = i - s_temp[-1]
                    s_temp.pop()
                s_temp.append(i)
            else:
                s_temp.append(i)

        return res

        # res = [0, 0, 0, 0, 0, 0, 0]
        # stack = [0]

        # stack = [0]

