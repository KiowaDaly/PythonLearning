class Solution:
    # this function is asuming that all are lowercase and no unicode characters exist in either string.
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

# solution found on leetcode with O(n)
# def isAnagram1(self, s, t):
#   return collections.Counter(s) == collections.Counter(t)

# my solution is O(n log n)

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("anagram", "car"))