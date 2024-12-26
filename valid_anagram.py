class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        
        return False
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
            
### Fastest 
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for w in set(s):
            if s.count(w)!=t.count(w):
                return False
        return True
    
#### OR 
from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    
    
class validAnagram:
    def solution(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 
        
        dict_s = dict()
        dict_t = dict()
        
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i],0) + 1 
            dict_t[t[i]] = dict_t.get(t[i],0) + 1 
        
        print(dict_s,"\n\n\n\n",dict_t)
        
        print(dict_s == dict_t)
                 
        for i in dict_t:
            if dict_t[i] != dict_s.get(i,0):
                return False 
        
        return True  
    
cls = validAnagram()
print(cls.solution(s='racecar', t='carrace'))