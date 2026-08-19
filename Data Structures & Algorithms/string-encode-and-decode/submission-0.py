class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ''
        for i in range(len(strs)):
            encode += str(len(strs[i]))
            encode += '#'
            encode += strs[i]
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i=0
        
        while i < len(s):
            j = i
            
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            word = s[j+1: length + j +1]
            decode.append(word)
            i = j+length+1
        return decode
            
            
            