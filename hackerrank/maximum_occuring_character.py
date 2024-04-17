"""
Given a string, return the character that appears the maximum number of times 
in the string. The string will contain only ASCII characters, from the ranges
('a'-'z','A'-'Z','0'-'9'), and case matters. If there is a tie in the maximum 
number of times a character appears in the string, return the character that 
appears first in the string.

Example: 
text = 'abbbaacc'

ans = 'a'
"""

def maximumOccurrinCharacter(text):
    hashset = {}
    for i in text:
        if i in hashset:
            continue
        hashset[i] = text.count(i)
    
    ans = sorted(hashset.items(), key=lambda x:x[1],reverse=True)[0][0]
    return ans 
         