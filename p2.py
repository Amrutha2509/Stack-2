class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if not stack:
                    return False
                res = stack.pop()
                if res + char not in ('()', '{}', '[]'):
                    return False
        return not stack
