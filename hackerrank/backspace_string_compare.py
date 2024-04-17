"""
Two strings are said to be the same if they are of the same length and have the same 
character at each index. Backspacing in a string removes the previous character 
in the string.

Given two strings containing lowercase English letters and the character '#' which 
represents a backspace key, determine if the two final strings are equal. Return
1 if they are equal or 0 if they are not. Note that backspacing an empty string 
results in an empty string.

Example:
s1 = 'axx#bb#c'
s2 = 'axbd#c#c'

Answer is 1 because after backspace processing both are the same. 
"""

def compareStrings(s1,s2):
    
    def string_processor(s):
        stack = []
        for i in s:
            if i == '#' and stack:
                stack.pop()
            elif i == '#':
                continue
            else:
                stack.append(i)
        if stack:
            return ''.join(stack)
        return ''

    if string_processor(s1) == string_processor(s2):
        return 1
    return 0

