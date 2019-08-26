class Solution:
    # Not allowed use + or - operators
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = a & b
            a ^= b
            b = carry << 1
        return a

    # code above takes too long to run

    # this code does the same recursively written by Kiowa and help from solutions to this problem on leetcode
    # There was an issue with negative numbers showing as Max integer size - that number
    # ie a massive number rather than say -20 it was 4294967276 so i added the masks into my own recursion algorithm!
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # SETTING UPPER LIMITS TO AVOID OVERFLOW
        max = 0x7FFFFFFF
        if b == 0:
            return a if a <= max else ~(a ^ mask)
        else:
            return self.getSum((a ^ b) & mask, ((a & b) << 1 ) & mask)


# same as recursive solution but iterative intstead
    def getSum(self, a: int, b: int) -> int:
        while a != 0:
            a, b = ((a & b) << 1, (a ^ b))
            a &= 0xFFFFFFFF
            b &= 0xFFFFFFFF
        return b

    # Correct answer below
# class Solution(object):
#     def getSum(self, a, b):
#         """
#         :type a: int
#         :type b: int
#         :rtype: int
#         """
#         # 32 bits integer max
#         MAX = 0x7FFFFFFF
#         # 32 bits interger min
#         MIN = 0x80000000
#         # mask to get last 32 bits
#         mask = 0xFFFFFFFF
#         while b != 0:
#             # ^ get different bits and & gets double 1s, << moves carry
#             a, b = (a ^ b) & mask, ((a & b) << 1) & mask
#         # if a is negative, get a's 32 bits complement positive first
#         # then get 32-bit positive's Python complement negative
#         return a if a <= MAX else ~(a ^ mask)