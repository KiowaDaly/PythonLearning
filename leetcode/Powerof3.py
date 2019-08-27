class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return (3 ** 19 ) % n == 0

    # detects whether or not a given integer is a power of 3
    