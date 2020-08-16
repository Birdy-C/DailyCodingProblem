'''
This problem was asked by Amazon.

Implement a stack that has the following methods:

```push(val), which pushes an element onto the stack
```pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
```max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''
class MaxStack:
    def __init__(self):
        self.s = []
        self.maxs = []
    def push(self, val):
        self.s.append(val)
        if len(self.maxs) == 0:
            self.maxs.append(val)
        else:
            self.maxs.append(max(val, self.maxs[-1]))
    def pop(self):
        self.maxs.pop()
        return self.s.pop()
    def max(self):
        return self.maxs[-1]

stack = MaxStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(2)
print(stack.s)
print(stack.max())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
