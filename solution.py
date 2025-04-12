from math import factorial
from collections import defaultdict, Counter

# Made by Coding Moves 🎯 | YouTube: Coding Moves | Subscribe for smart coding!
class Solution(object):
    def countGoodIntegers(self, n, k):
        palindromes = set()
        
        def generate_palindromes():
            half_len = (n + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            for first_half in range(start, end):
                first_half_str = str(first_half)
                if n % 2 == 0:
                    palindrome_str = first_half_str + first_half_str[::-1]
                else:
                    palindrome_str = first_half_str + first_half_str[:-1][::-1]
                palindrome = int(palindrome_str)
                if palindrome % k == 0:
                    palindromes.add(palindrome_str)
        
        generate_palindromes()
        
        multisets = set()
        for p in palindromes:
            cnt = tuple(sorted(Counter(p).items()))
            multisets.add(cnt)
        
        total = 0
        for ms in multisets:
            digits = []
            total_digits = 0
            for d, cnt in ms:
                digits.append((int(d), cnt))
                total_digits += cnt
            assert total_digits == n
            
            numerator = factorial(n)
            denominator = 1
            lead_digit_options = 0
            for d, cnt in digits:
                denominator *= factorial(cnt)
                if d != 0:
                    lead_digit_options += cnt
            if lead_digit_options == 0:
                continue
            total_arrangements = numerator // denominator
            valid_arrangements = total_arrangements * lead_digit_options // n
            total += valid_arrangements
        
        return total
