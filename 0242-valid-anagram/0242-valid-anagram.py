class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        if(set(s) != set(t)):
            return False
        letters = {}
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        for i in t:
            if i in letters:
                letters[i] -= 1
                if letters[i] < 0:
                    return False
            else:
                return False
        return True
        
        