#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    // Yordamchi funksiya: Markazdan kengaytirib eng uzun palindrom substringni topish
    string expandAroundCenter(const string& s, int left, int right) {
        // Chap va o'ng tomondan kengaytirish
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        // Oxirgi to'g'ri palindrom substringni qaytarish
        return s.substr(left + 1, right - left - 1);
    }

    string longestPalindrome(string s) {
        // Agar matn uzunligi 1 yoki kam bo'lsa, o'zi palindrom
        if (s.length() < 2) {
            return s;
        }

        string longestPalindrome = "";
        for (int i = 0; i < s.length(); i++) {
            // 1. Belgini markaz qilib kengaytirish
            string oddPalindrome = expandAroundCenter(s, i, i);
            // 2. Harf juftligini markaz qilib kengaytirish
            string evenPalindrome = expandAroundCenter(s, i, i + 1);

            // Eng uzun palindromni yangilash
            if (oddPalindrome.length() > longestPalindrome.length()) {
                longestPalindrome = oddPalindrome;
            }
            if (evenPalindrome.length() > longestPalindrome.length()) {
                longestPalindrome = evenPalindrome;
            }
        }

        return longestPalindrome;
    }
};

// Misollarni tekshirish
int main() {
    Solution solution;
    cout << solution.longestPalindrome("babad") << endl;  // Output: "bab" yoki "aba"
    cout << solution.longestPalindrome("cbbd") << endl;   // Output: "bb"
    return 0;
}
