text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel." \
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

new_text = text.split()

list_text = []

for word in new_text:
    if word.endswith(',') or word.endswith('.'):
        sign = word[-1]
        clean_text = word[:-1]
        new_word = clean_text + "ing" + sign
    else:
        new_word = word + "ing"
    list_text.append(new_word)
result = ' '.join(list_text)
print(result)
