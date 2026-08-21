class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        flip = {}
        for key in freq:
            value = freq[key]
            if value not in flip:
                flip[value] = []
            flip[value].append(key)
        res = []
        for i in sorted(flip):
            for j in flip[i]:
                res.append(j)
        return res[-k:]