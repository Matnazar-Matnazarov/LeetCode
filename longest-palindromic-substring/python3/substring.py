class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Eng uzun palindrom bo'lgan substringni topish uchun yordamchi funksiya
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Kengaytirish tugagandan keyin, oxirgi to'g'ri palindrom substringni qaytaradi
            return s[left + 1:right]
        
        # Edge case: agar matn uzunligi 1 yoki kam bo'lsa, matnning o'zi palindrom
        if len(s) < 2:
            return s

        longest_palindrome = ""
        for i in range(len(s)):
            # 1. Belgini markaz qilib kengaytirish
            odd_palindrome = expandAroundCenter(i, i)
            # 2. Harf juftligini markaz qilib kengaytirish
            even_palindrome = expandAroundCenter(i, i + 1)

            # Eng uzun palindromni yangilash
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
        
        return longest_palindrome

# Misollarni tekshirish
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" yoki "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"
