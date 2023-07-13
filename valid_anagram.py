class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        string_1 = list(s)
        string_2 = list(t)
        string_1.sort()
        string_2.sort()
        if string_1 == string_2:
            return True
        else:
            return False
        