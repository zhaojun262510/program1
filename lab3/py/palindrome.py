def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # 输出：True
print(is_palindrome("hello"))    # 输出：False