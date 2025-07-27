class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: only one row
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False

        # Build rows in zigzag order
        for char in s:
            rows[current_row] += char
            # Change direction when reaching top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Join all rows
        return "".join(rows)

        