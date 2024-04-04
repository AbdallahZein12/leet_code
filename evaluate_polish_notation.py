### Faster solution
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []
        
        opp = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: x - y,
            '*': lambda x,y: x * y,
            '/': lambda x,y: int(x/y)
        }

        for i in tokens:
            res = i
            if i in opp:
                res = opp[i](stack.pop(-2),stack.pop(-1))
            stack.append(int(res))

        return stack[0]

####

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "+":
                    stack.append(first+second)
                elif token == "-":
                    stack.append(first-second)
                elif token == "/":
                    stack.append(first/second)
                else:
                    stack.append(first*second)
            else:
                stack.append(token)
        return int(stack[0])
    
###

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []
        
        for i in tokens:
            if i in ['+','-','*','/']:    
                result = int(eval(f"{stack.pop(-2)} {i} {stack.pop()}"))
                stack.append(result)
            else:
                stack.append(i)

        return int(stack[-1])
    
####




import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(i)
            else:
                if i == '/':
                    result = math.trunc(eval(f"{stack.pop(-2)} {i} {stack.pop()}"))
                else:
                    result = eval(f"{stack.pop(-2)} {i} {stack.pop()}")
                stack.append(result)

        return int(stack[-1])
        