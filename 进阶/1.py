import re
from collections import Counter

word = open('word.txt', 'r', encoding='UTF-8')
words = word.read()
word_list = re.split(' ', words)
word_most = Counter(word_list).most_common(2)
print(word_most)
