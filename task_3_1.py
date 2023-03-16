s = input("Введите строку: \n")
s = s.split(" ")
new_words = []
repl = [".", ",", "?", "!"]
for word in s:
    for x in repl:
        word = word.replace(x, "")
    # print(word)
    if len(word) > 5:
        new_words.append(word)
print(" ".join(new_words))
