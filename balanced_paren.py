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
                
            
                