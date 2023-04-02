import re

my_word = 'Muffet'
paragraph = """Little Miss Muffet sat on a tuffet,
Eating her curds and whey,
Then came along came a spider who sat down beside her,
And frightened Miss Muffet away!"""

d = {}

def word_length(w, p):
    text = re.sub(r'[^a-zA-Z0-9\s]+', '', p).lower().split()
    w = w.lower()
    for i in text:
        if i not in d:
            d[i] = len(i)

    len_words = [x for x in text if len(x) == len(w)]
    return w, d[w], len(len_words), len_words

word, letter_count, paragraph_count, words = word_length(my_word, paragraph)

print(f"The word '{word}' has {letter_count} characters. \n"
      f"Words of that length appear {paragraph_count} times in the paragraph. \n")

# x = word_length('miss', paragraph)
# print(x[0], x[1], x)
