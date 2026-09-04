class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[ch for ch in s if ch.isalnum()]
        s=''.join(s).lower()
        i = 0
        j = len(s) -1
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True