class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','')
        s = ''.join(b.lower() for b in s if b.isalnum())
        b = s[::-1]

        for i in range(len(s)):
            if s[i] == b[i]:
                continue
            else:
                return False
        return True