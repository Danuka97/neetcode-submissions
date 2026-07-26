class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        reversed_s = clean_s[::-1]

        return reversed_s == clean_s