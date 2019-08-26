class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


sol = Solution()
print(sol.isPalindrome(123))