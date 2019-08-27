class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count_open = 0
        count_close = 0
        temp_string = ''
        final_string = ""
        for c in S:
            if c == '(':
                count_open += 1
                temp_string += c
            if c == ')':
                count_close += 1
                temp_string += c
            if count_close == count_open and count_close > 0:
                final_string += temp_string[1:-1]
                temp_string = ''

        return final_string


sol = Solution()
print(sol.removeOuterParentheses('(()())(())'))
