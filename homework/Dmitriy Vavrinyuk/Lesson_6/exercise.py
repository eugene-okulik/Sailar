# Задание 1
# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero” и после этого выводит получившийся текст на экран. Знаки препинания не должны оказаться
# внутри слова. Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
# но уже преобразованного.

initial_sentences = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
                     'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

modife_senteces = []

sentences = initial_sentences.split()
for sentence in sentences:
    if ',' in sentence:
        sentence = sentence.replace(',', '')
        sentence += "ing,"
    elif '.' in sentence:
        sentence = sentence.replace(',', '')
        sentence += "ing."
    else:
        sentence += "ing"
    modife_senteces += [sentence]

modife_senteces = ' '.join(modife_senteces)
print(modife_senteces)
