class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        if num >= 2**31 -1:
            return 0
        if x < 0:
            if num >= 2**31:
                return 0
            return num*-1
        return num


sol = Solution()
print(sol.reverse(-123))