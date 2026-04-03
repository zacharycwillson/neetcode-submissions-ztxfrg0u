class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            length = 1
            if (num - 1) not in num_set and (num + 1) in num_set:
                length = 2
                next_num = num + 1
                while (next_num + 1) in num_set:
                    length += 1
                    next_num += 1
            max_length = max(max_length, length)
        return max_length  
                

        