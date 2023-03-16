s = input("Введите строку: \n")
s = s.split()
new_words = []
for words in s:
    if len(words) > 5:
        new_words.append(words)
print(" ".join(new_words))
