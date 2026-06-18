class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = "".join(filter(str.isalnum, s.lower()))
        return normalized == normalized[::-1]
        