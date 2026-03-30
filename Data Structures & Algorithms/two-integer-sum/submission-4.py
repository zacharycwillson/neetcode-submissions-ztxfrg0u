class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, num in enumerate(nums):
            sum2 = target - num
            if sum2 in hash:
                return [hash[sum2], i]
            hash[num] = i
        
        