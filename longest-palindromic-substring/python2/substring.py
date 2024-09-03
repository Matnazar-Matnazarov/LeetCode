class Solution:
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if not s:
            return ""

        longest_palindrome = ""
        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            
            # Check for even-length palindromes
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome