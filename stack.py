class Stack:
    def __init__(self):
        self.stack = [] 
    
    def push(self, item):
        self.stack.append(item) # appends 'item' to the end of the list named 'stack'

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    # if stack is not empty then remove item at the top of the stack, otherwise do nothing
    
    def is_empty(self):
        return len(self.stack) == 0 # return stack if size is 0