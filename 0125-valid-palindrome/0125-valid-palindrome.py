class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        processed = ""
        reverse = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                processed += s[i].lower()
                reverse = s[i].lower() + reverse
        return processed == reverse
        
        