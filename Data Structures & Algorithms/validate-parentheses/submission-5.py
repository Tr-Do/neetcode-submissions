class Solution:
    def isValid(self, s: str) -> bool:
        s1 = ['(','[','{']
        s2 = [')',']','}']
        stack = []
        for ch in s:
            if ch in s1:
                stack.append(s2[s1.index(ch)])
            else:
                if not stack:
                    return False
                elif ch != stack.pop():
                    return False
        return False if stack else True