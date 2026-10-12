class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        count = Counter(nums)
        n = len(nums)
        freq = [[] for _ in range(n+1) ]
        for key, value in count.items():
            freq[value].append(key)
        res = []
        for i in range(n, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res