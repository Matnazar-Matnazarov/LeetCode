public class Solution {
    // Yordamchi funksiya: Markazdan kengaytirib eng uzun palindrom substringni topish
    private String expandAroundCenter(String s, int left, int right) {
        // Chap va o'ng tomondan kengaytirish
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // Oxirgi to'g'ri palindrom substringni qaytarish
        return s.substring(left + 1, right);
    }

    public String longestPalindrome(String s) {
        // Agar matn uzunligi 1 yoki kam bo'lsa, o'zi palindrom
        if (s.length() < 2) {
            return s;
        }

        String longestPalindrome = "";
        for (int i = 0; i < s.length(); i++) {
            // 1. Belgini markaz qilib kengaytirish
            String oddPalindrome = expandAroundCenter(s, i, i);
            // 2. Harf juftligini markaz qilib kengaytirish
            String evenPalindrome = expandAroundCenter(s, i, i + 1);

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

    // Asosiy metod: Sinovni amalga oshirish
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Misollar
        String[] testCases = {
            "babad",
            "cbbd",
            "a",
            "ac",
            "racecar",
            "abccba"
        };

        for (String testCase : testCases) {
            System.out.println("Input: \"" + testCase + "\"");
            System.out.println("Longest Palindromic Substring: \"" + solution.longestPalindrome(testCase) + "\"");
            System.out.println();
        }
    }
}
