class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freq = Counter(nums)
        pairs = []
        for key, value in freq.items():
            pairs.append((value,key))
        pairs.sort(reverse = True)
        res = []
        for i in range(k):
            res.append(pairs[i][1])
        return res