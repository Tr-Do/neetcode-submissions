class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            re = target - nums[i]
            if re in res:
                return [res[re], i]
            res[nums[i]] = i