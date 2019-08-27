class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(i) for i in J)


sol = Solution()
print(sol.numJewelsInStones("Aa", "aAAbbbbb"))
