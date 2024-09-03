# 🚀 Longest Palindromic Substring

[![C++](https://img.shields.io/badge/C%2B%2B-%238732bf.svg?style=for-the-badge&logo=cplusplus&logoColor=white)](https://en.wikipedia.org/wiki/C%2B%2B)
[![Python](https://img.shields.io/badge/Python-%233877ab.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-%23007396.svg?style=for-the-badge&logo=java&logoColor=white)](https://www.java.com/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange?style=for-the-badge)](https://leetcode.com/)

## 📝 Problem Description

Given a string `s`, return the longest palindromic substring in `s`.

### Example 1:
- **Input:** `s = "babad"`
- **Output:** `"bab"` or `"aba"`

### Example 2:
- **Input:** `s = "cbbd"`
- **Output:** `"bb"`

### Constraints:
- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

## 💡 Algorithm Explanation

The solution employs various algorithms to find the longest palindromic substring efficiently. Implementations are available in multiple languages including Python, Java, and C++.

### Approach:
- **Expand Around Center:** Treat each character and each pair of characters as the center of a potential palindrome and expand outward.
- **Dynamic Programming:** Use a 2D table to store information about palindromic substrings.
- **Manacher's Algorithm:** An advanced algorithm that finds the longest palindromic substring in linear time.

## 🔍 Complexity:
- **Time Complexity:** Varies depending on the algorithm used (O(n^2) for Expand Around Center, O(n^2) for Dynamic Programming, O(n) for Manacher's Algorithm).
- **Space Complexity:** O(1) for Expand Around Center, O(n^2) for Dynamic Programming, O(n) for Manacher's Algorithm.

## 🛠️ Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Matnazar-Matnazarov/LeetCode.git
