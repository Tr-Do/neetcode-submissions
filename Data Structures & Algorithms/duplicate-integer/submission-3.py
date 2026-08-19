class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = dict()
        for i in nums:
            if i in a:
                a[i] += 1
                if a[i] > 1:
                    return True
            else:
                a[i] = 1
        return False