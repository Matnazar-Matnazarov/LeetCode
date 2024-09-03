#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        // Agar faqat 1 qator yoki matn uzunligi 1 bo'lsa, oddiy holat
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        // Har bir qatorda joylashtiriladigan belgilarni saqlash uchun vektor
        vector<string> rows(min(numRows, int(s.length())));
        int currentRow = 0;
        bool goingDown = false;

        // Har bir belgi uchun tegishli qatorga joylashtirish
        for (char c : s) {
            rows[currentRow] += c;
            // 1-qatordan oxirgi qatorgacha pastga va yuqoriga harakat qilish
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }
            currentRow += goingDown ? 1 : -1;
        }

        // Natijaviy satrni yaratish
        string result;
        for (string row : rows) {
            result += row;
        }
        return result;
    }
};

// Misollarni tekshirish
int main() {
    Solution solution;
    cout << solution.convert("PAYPALISHIRING", 3) << endl;  // Output: "PAHNAPLSIIGYIR"
    cout << solution.convert("PAYPALISHIRING", 4) << endl;  // Output: "PINALSIGYAHRPI"
    cout << solution.convert("A", 1) << endl;               // Output: "A"
    return 0;
}
