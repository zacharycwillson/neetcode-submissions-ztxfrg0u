class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
            
        sHash = {}
        tHash = {}

        for char in s:
            if char in sHash:
                sHash[char] += 1
            else:
                sHash[char] = 1
        for char in t:
            if char in tHash:
                tHash[char] += 1
            else:
                tHash[char] = 1
        return sHash == tHash

        