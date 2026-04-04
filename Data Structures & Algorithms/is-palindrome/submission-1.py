class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        for char in s:
            if not char.isalnum():
                continue
            forward += char.lower()
        reverse = forward[::-1]
        if forward == reverse:
            return True
        return False

        

        