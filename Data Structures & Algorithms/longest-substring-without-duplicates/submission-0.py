class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        subs = set()
        max_length = 0
        for i in range(len(s)):
            while s[i] in subs:
                subs.remove(s[l])
                l += 1
            subs.add(s[i])
            max_length = max(max_length, i-l+1)
        return max_length
