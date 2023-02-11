class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def step(n):
            retval = 0
            while n != 0:
                retval += (n % 10) * (n % 10)
                n = n // 10
            return retval
        fast_p = n
        slow_p = n
        while fast_p != 1 and step(fast_p) != 1:
            fast_p = step(step(fast_p))
            slow_p = step(slow_p)
            if fast_p == slow_p:
                return False
        return True
        