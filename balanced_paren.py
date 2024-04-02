## Newest Solution

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        valid_paren = {'(':')', '[':']','{':'}'}

        for i in s:
            if i in valid_paren:
                stack.append(i)
            else:
                if not stack:
                    return False
                if valid_paren[stack[-1]] != i:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False

        return True
                

### Older solution


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        def is_balanced(top, bracket):
            if top == "(" and bracket == ")":
                return True
            elif top == "[" and bracket == "]":
                return True
            elif top == "{" and bracket == "}":
                return True 
            else:
                return False

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack: 
                    return False
                if is_balanced(stack.pop(),i) == False:
                    return False
                    



        if not stack:
            return True
                
            
