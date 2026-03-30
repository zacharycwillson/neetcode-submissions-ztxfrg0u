class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set(nums)
        if len(dup_set) == len(nums):
            return False
        return True
        