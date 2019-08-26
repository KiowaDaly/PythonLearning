class Solution:
    def romanToInt(self, s: str) -> int:
        # Loop each character and add value from hash map to counter.
        #
        # this code is a solution written by "agave" on https://leetcode.com/problems/roman-to-integer/discuss/6542/4-lines-in-Python
        roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        count, p = 0, "I"

        for c in s[::-1]:
            count = count - roman_numerals[c] if roman_numerals[c] < roman_numerals[p] else count + roman_numerals[c]
            p = c
        return count


sol = Solution()
print(sol.romanToInt("IX"))
