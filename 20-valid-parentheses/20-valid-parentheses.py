class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in valid:  
                stack.append(i)
            elif len(stack) == 0 or valid[stack.pop()] != i:  
                return False
        return len(stack) == 0 