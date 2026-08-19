# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        pos = 0
        result = []
        n = len(pairs)
        if n == 0:
            return pairs
        else:
            result.append(pairs[:])
            for i in range(1,n):
                for j in range(i-1, -1, -1):
                    if pairs[i].key >= pairs[j].key:
                        pos = j+1
                        break
                pairs.insert(pos,pairs[i])
                pairs.pop(i+1)
                pos=0
                result.append(pairs[:])
            return result