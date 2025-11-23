# Secure Coding Review Report

## Application: Flask Sample App
## Date: 23.11.2025

### 🔴 Finding 1 — SQL Injection
- File: app.py
- Line: 13
- Risk: High
- Description:
  User input `username` is directly inserted into SQL query.
- Recommendation:
  Use parameterized queries:
  cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
