class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        distinct = set(nums)
        fre_dict = {num:0 for num in distinct}

        for key in fre_dict:
            fre_dict[key] = nums.count(key)
        
        sort_key = sorted(fre_dict, key=fre_dict.get, reverse=True)
        return sort_key[:k]