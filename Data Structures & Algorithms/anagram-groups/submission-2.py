class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs: 
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            res[key].append(string)
        return list(res.values())
        