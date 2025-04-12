# 🚀 LeetCode 3272 - Count of Good Integers

> 🔧 Difficulty: Hard  
> 💡 Topic: Palindromes, Permutations, Counting, Math, Combinatorics  
> 🎥 From: [Coding Moves - YouTube Channel](https://youtube.com/@Coding_Moves)

---

## 🧠 Problem Summary

You are given two positive integers `n` and `k`.

An integer `x` is called **k-palindromic** if:
- `x` is a palindrome.
- `x` is divisible by `k`.

An integer is called **good** if its digits can be **rearranged** to form a **k-palindromic** integer.

**Return** the count of all **good integers** with exactly `n` digits and no leading zero.

---

## 🧪 Examples

### Example 1:
#### Input: n = 3, k = 5
#### Output: 27


---

## 🧩 Key Constraints
- `1 <= n <= 10`
- `1 <= k <= 9`

---

## 🧑‍💻 Solution Strategy

1. **Generate all `n`-digit palindromes** using half-construction.
2. Filter the ones divisible by `k` (i.e., **k-palindromes**).
3. For each unique digit multiset of those palindromes:
   - Count how many permutations of those digits are valid `n`-digit numbers (no leading zero).
4. Use factorial math for efficient permutation counting.

---

## 📦 How to Run

```bash
python solution.py
```
# 🎬 Follow Us
## 📺 Coding Moves
## 🎓 Helping You Move Smart in Code
## 🔗 YouTube.com/@Coding_Moves
