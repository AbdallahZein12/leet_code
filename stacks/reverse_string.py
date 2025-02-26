"""
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.

This will use the Stack class
"""


class Stack: 
    def __init__(self):
        self.stack_list = []
    
    def print_stack(self):
        for i in range(len(self.stack_list)-1,-1,-1):
            print(self.stack_list[i])
            
    def is_empty(self):
        return len(self.stack_list) == 0 

    def peek(self):
        if self.is_empty():
            return None 
        else:
            return self.stack_list[-1]
        
    def size(self):
        return len(self.stack_list)
    
    def push(self, value):
        self.stack_list.append(value)
        
    def pop(self):
        if self.is_empty():
            return None 
        else:
            return self.stack_list.pop()
        

def reverse_string(s):
    if len(s) <= 1:
        return s 
    
    stack = Stack() 
    for i in s:
        stack.push(i)
    result = '' 
    for i in range(stack.size()): 
        result += stack.pop() 
    return result