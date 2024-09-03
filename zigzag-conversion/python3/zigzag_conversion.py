class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Agar faqat 1 qator yoki matn uzunligi 1 bo'lsa, oddiy holat
        if numRows == 1 or numRows >= len(s):
            return s

        # Har bir qatorda joylashtiriladigan belgilarni saqlash uchun massiv
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Har bir belgi uchun tegishli qatorga joylashtirish
        for char in s:
            rows[current_row] += char
            # 1-qatordan oxirgi qatorgacha pastga va yuqoriga harakat qilish
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Natijaviy satrni yaratish
        return ''.join(rows)

# Misollarni tekshirish
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))               # Output: "A"
