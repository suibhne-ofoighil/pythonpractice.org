word = input('enter word to palindrummer: ')
if len(word) < 1: word = 'radar'
word = str(word.lower())
rvs=(word[::-1])

if rvs == word: print(word, 'is a palindrom!')
else: print(word,'≠', rvs)




