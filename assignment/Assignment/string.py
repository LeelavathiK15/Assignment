def is_palindrome(s):
    s = s.lower()
    reversed_s = s[::-1]
    return s == reversed_s
print(is_palindrome(input()))