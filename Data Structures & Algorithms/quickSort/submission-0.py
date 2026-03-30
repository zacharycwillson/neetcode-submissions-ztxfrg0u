# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    
    def quickSortHelper(self, pairs, s: int, e: int):
        # Base case, subarray is length 1
        if (e - s) <= 0:
            return
        
        pivot = pairs[e]
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = tmp
                left += 1
        
        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)
        return
        

        


        