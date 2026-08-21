class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            a = len(word)
            b = '#'
            encoded += str(a)+b+word
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        num = ''
        while i < len(s):
            ch = ''
            if s[i].isdigit():
                num += s[i]
                i += 1
            else:
                num = int(num)
                ch = s[i+1:i+1+num]
                decoded.append(ch)
                i = i+1+num
                num = ''
        return decoded