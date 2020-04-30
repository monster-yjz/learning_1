words = ['apple', 'best', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    # 　根据字母将列表转为字典
    by_letter.setdefault(letter, []).append(word)

print(by_letter)
