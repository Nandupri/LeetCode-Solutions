class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Step 1: Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Determine sign
        sign = 1
        index = 0
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            index += 1

        # Step 3: Convert digits
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])

            # Step 4: Check overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            index += 1

        return sign * result
