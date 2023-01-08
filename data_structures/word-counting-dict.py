sentence = """A horse is a horse, of course, of course,
And no one can talk to a horse of course,
That is, of course, unless the horse is the famous Mr. Ed."""

sentence = sentence.replace(',', '').lower().split()
wc = {}

for word in sentence:
    if word in wc.keys():
        wc[word] += 1
    else:
        wc[word] = 1

print(wc)
