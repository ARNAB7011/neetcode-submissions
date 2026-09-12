class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and convert to lowercase
        s = ''.join(ch.lower() for ch in s if ch.isalnum())

        # Check if string is same forward and backward
        return s == s[::-1]