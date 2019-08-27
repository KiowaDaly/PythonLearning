class Solution:
    def isPalindrome(self, s: str) -> bool:
            s = [c.lower() for c in s if c.isalnum()]
            return s == s[::-1]

    # this algorithm removes all non alpha-numeric values using isalnum and then uses the reglar palindrome check with reversed string