class Solution {
    public String convert(String s, int numRows) {
        // Agar faqat 1 qator yoki matn uzunligi 1 bo'lsa, oddiy holat
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        // Har bir qatorda joylashtiriladigan belgilarni saqlash uchun ro'yxat
        StringBuilder[] rows = new StringBuilder[Math.min(numRows, s.length())];
        for (int i = 0; i < rows.length; i++) {
            rows[i] = new StringBuilder();
        }

        int currentRow = 0;
        boolean goingDown = false;

        // Har bir belgi uchun tegishli qatorga joylashtirish
        for (char c : s.toCharArray()) {
            rows[currentRow].append(c);
            // 1-qatordan oxirgi qatorgacha pastga va yuqoriga harakat qilish
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }
            currentRow += goingDown ? 1 : -1;
        }

        // Natijaviy satrni yaratish
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }
        return result.toString();
    }

    // Misollarni tekshirish
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.convert("PAYPALISHIRING", 3));  // Output: "PAHNAPLSIIGYIR"
        System.out.println(solution.convert("PAYPALISHIRING", 4));  // Output: "PINALSIGYAHRPI"
        System.out.println(solution.convert("A", 1));               // Output: "A"
    }
}
