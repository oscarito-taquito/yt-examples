# return the unique set of letters in a word
word = 'mississippi'
lst = set(word)
letters = ''.join(map(str, lst))
print(letters)