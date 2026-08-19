class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            sortt = "".join(sorted(i))
            d[sortt].append(i)
        return list(d.values())