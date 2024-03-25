class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        if s[0] in ('-', '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        result *= sign
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result