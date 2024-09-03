<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Longest Palindromic Substring</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f8f9fa;
        }
        h1, h2, h3 {
            color: #343a40;
        }
        .badge {
            font-size: 12px;
            font-weight: bold;
            color: #fff;
            text-decoration: none;
            margin-right: 5px;
        }
        .badge-blue { background-color: #007bff; }
        .badge-yellow { background-color: #ffc107; }
        .badge-green { background-color: #28a745; }
        .badge-lightgrey { background-color: #f8f9fa; }
        .code-block {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: monospace;
            white-space: pre;
        }
        .highlight {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .icon-container img {
            height: 50px;
            margin: 5px;
            transition: transform 0.5s, filter 0.5s;
        }
        .icon-container img.cpp-icon {
            filter: hue-rotate(270deg);
        }
        .animated-text {
            font-size: 24px;
            color: #007bff;
            animation: pulse 1.5s infinite, color-change 3s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        @keyframes color-change {
            0% { color: #007bff; }
            50% { color: #0056b3; }
            100% { color: #007bff; }
        }
        .btn-custom {
            background-color: #5732de;
            color: white;
        }
        .btn-custom:hover {
            color: darkblue;
            background-color: #5732de;
        }
    </style>
</head>
<body>

<div class="container">
    <h1 class="animated-text">🚀 Longest Palindromic Substring</h1>

    <a href="#" class="badge" style="background-color: #8732bf;">C++</a>
    <a href="#" class="badge btn-custom">Python</a>
    <a href="#" class="badge badge-warning">Java</a>
    <a href="#" class="badge badge-success">LeetCode Medium</a>

    <h2>📝 Problem Description</h2>
    <p>Given a string <code>s</code>, return the longest palindromic substring in <code>s</code>.</p>

    <h3>Example 1:</h3>
    <ul>
        <li><strong>Input:</strong> <code>s = "babad"</code></li>
        <li><strong>Output:</strong> <code>"bab"</code> or <code>"aba"</code></li>
    </ul>

    <h3>Example 2:</h3>
    <ul>
        <li><strong>Input:</strong> <code>s = "cbbd"</code></li>
        <li><strong>Output:</strong> <code>"bb"</code></li>
    </ul>

    <h3>Constraints:</h3>
    <ul>
        <li><code>1 <= s.length <= 1000</code></li>
        <li><code>s</code> consists of only digits and English letters.</li>
    </ul>

    <p><a href="https://leetcode.com/problems/longest-palindromic-substring/" class="btn btn-primary">Problem Link</a></p>

    <h2>💡 Algorithm Explanation</h2>
    <p>The solution employs various algorithms to find the longest palindromic substring efficiently. Implementations are available in multiple languages including Python, Java, and C++.</p>

    <h3>Approach:</h3>
    <ul>
        <li><strong>Expand Around Center:</strong> Treat each character and each pair of characters as the center of a potential palindrome and expand outward.</li>
        <li><strong>Dynamic Programming:</strong> Use a 2D table to store information about palindromic substrings.</li>
        <li><strong>Manacher's Algorithm:</strong> An advanced algorithm that finds the longest palindromic substring in linear time.</li>
    </ul>

    <div class="highlight">
        <h4>Complexity:</h4>
        <ul>
            <li><strong>Time Complexity:</strong> Varies depending on the algorithm used (O(n<sup>2</sup>) for Expand Around Center, O(n<sup>2</sup>) for Dynamic Programming, O(n) for Manacher's Algorithm).</li>
            <li><strong>Space Complexity:</strong> O(1) for Expand Around Center, O(n<sup>2</sup>) for Dynamic Programming, O(n) for Manacher's Algorithm.</li>
        </ul>
    </div>

    <h2>🛠️ Getting Started</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre class="code-block">git clone https://github.com/Matnazar-Matnazarov/LeetCode.git</pre>
        </li>
        <li><strong>Navigate to Directory:</strong>
            <pre class="code-block">cd LeetCode</pre>
        </li>
        <li><strong>Install Dependencies:</strong> (if applicable)</li>
        <li><strong>Run the Solution:</strong> Depending on the language, use appropriate commands to compile or execute the code.</li>
    </ol>

    <h2>📝 License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>🤝 Contributing</h2>
    <p>Contributions are welcome! Please submit a Pull Request to propose changes or improvements.</p>

    <h2>📧 Contact</h2>
    <p>For questions or suggestions, please contact me at <a href="mailto:matnazarmatnazarov3@gmail.com">matnazarmatnazarov3@gmail.com</a>.</p>

    <div class="icon-container" align="center">
        <img src="https://skillicons.dev/icons?i=python" alt="Python Icon" />
        <img src="https://skillicons.dev/icons?i=cpp" alt="C++ Icon" class="cpp-icon" />
        <img src="https://skillicons.dev/icons?i=java" alt="Java Icon" />
    </div>
</div>

<!-- Bootstrap JS and dependencies -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

<!-- JavaScript for animations -->
<script>
    // Animated text and icon effects
    document.querySelector('.animated-text').addEventListener('mouseover', function() {
        this.style.color = '#0056b3';
        this.style.textShadow = '2px 2px 5px rgba(0, 0, 0, 0.3)';
    });
    document.querySelector('.animated-text').addEventListener('mouseout', function() {
        this.style.color = '#007bff';
        this.style.textShadow = 'none';
    });

    // Animate icon images
    document.querySelectorAll('.icon-container img').forEach(img => {
        img.addEventListener('mouseover', () => {
            img.style.transform = 'scale(1.2)';
            img.style.filter = 'brightness(1.2)';
        });
        img.addEventListener('mouseout', () => {
            img.style.transform = 'scale(1)';
            img.style.filter = 'brightness(1)';
        });

        // Continuous animation effect for icons
        setInterval(() => {
            img.style.transition = 'transform 0.5s ease, filter 0.5s ease';
            img.style.transform = 'rotate(360deg) scale(1.1)';
            setTimeout(() => {
                img.style.transform = img.style.transform = 'rotate(0deg) scale(1)';
            }, 500);
        }, 3000);
    });
</script>
</body>
</html>

