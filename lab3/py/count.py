def ccount(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count

print(ccount("hello world")) # 输出：{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}