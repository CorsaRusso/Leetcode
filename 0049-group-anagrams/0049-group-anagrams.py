class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        retval = []
        viewed = {}
        for i in strs:
            cur_sorted_str = ''.join(sorted(i))
            if cur_sorted_str in viewed:
                retval[viewed[cur_sorted_str]].append(i)
            else:
                viewed[cur_sorted_str] = len(retval)
                retval.append([i])
        return retval
                
            
        