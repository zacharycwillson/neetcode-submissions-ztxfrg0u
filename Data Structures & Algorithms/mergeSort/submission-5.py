# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int):
        #Base case
        if (e - s) <= 0:
            return pairs
        
        m = (s + e) // 2
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m+1, e)
        self.merge(pairs, s, m, e)
    
    def merge(self, pairs: List[Pair], s: int, m: int, e: int):
        left = pairs[s:m+1]
        right = pairs[m+1:e+1]
        i = j = 0
        k = s

        while i < len(left) and j < len(right):
            if left[i].key > right[j].key:
                pairs[k] = right[j]
                j += 1
            else:
                pairs[k] = left[i]
                i += 1
            k +=1

        while i < len(left):
            pairs[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            pairs[k] = right[j]
            j += 1
            k += 1
        
