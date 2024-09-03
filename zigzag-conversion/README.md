# 🚀 Zigzag Conversion

[![C++](https://img.shields.io/badge/C%2B%2B-%238732bf.svg?style=for-the-badge&logo=cplusplus&logoColor=white)](https://en.wikipedia.org/wiki/C%2B%2B)
[![Python](https://img.shields.io/badge/Python-%233877ab.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-%23007396.svg?style=for-the-badge&logo=java&logoColor=white)](https://www.java.com/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange?style=for-the-badge)](https://leetcode.com/problems/zigzag-conversion/)
## 📝 Problem Description

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows as shown below. Then, the pattern is read line by line.

For example, the zigzag pattern for the input string `"PAYPALISHIRING"` with 3 rows is:


Read line by line, the output will be: `"PAHNAPLSIIGYIR"`.

### Problem Statement

Write a function that converts a given string into a zigzag pattern based on the specified number of rows, then read line by line to form the output string.

- **Function Signature:**  
  `string convert(string s, int numRows);`

### Examples

**Example 1:**
- **Input:** `s = "PAYPALISHIRING"`, `numRows = 3`
- **Output:** `"PAHNAPLSIIGYIR"`

**Example 2:**
- **Input:** `s = "PAYPALISHIRING"`, `numRows = 4`
- **Output:** `"PINALSIGYAHRPI"`

**Explanation:**

**Example 3:**
- **Input:** `s = "A"`, `numRows = 1`
- **Output:** `"A"`

### Constraints:
- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','`, and `'.'`.
- `1 <= numRows <= 1000`

## 💡 Algorithm Explanation

### Approach

1. **Basic Idea:** Place characters in a zigzag pattern across multiple rows. Traverse through the rows and form the output string by reading line by line.
2. **Tracking Direction:** Use a flag to toggle between moving "down" and "up" in the zigzag pattern.
3. **Edge Case:** If `numRows` is 1, the output is the input string itself, as there is no zigzag pattern with a single row.

### Complexity Analysis
- **Time Complexity:** O(n), where n is the length of the string.
- **Space Complexity:** O(n), to store the characters in the rows.

## 🛠️ Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Matnazar-Matnazarov/LeetCode.git
   cd LeetCode/zigzag-conversion
