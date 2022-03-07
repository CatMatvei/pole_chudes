import random


with open("C:\\Matvey\\Programm\\Python\\dop\\text\\russian_nouns.txt", encoding='utf-8') as file:
	word_list = [row.strip() for row in file]
new_file = open('C:\\Matvey\\Programm\\Python\\dop\\text\\text.txt', 'w')

n = len(word_list)
new_list = []


for i in range(n):
	this_word = word_list[i]
	if len(this_word) <= 10 and len(this_word) > 2 and this_word.find('-') == -1:
		new_list.append(this_word)

for i in range(len(new_list)):
	new_file.write(new_list[i] + '\n')

# py C:\\Matvey\Programm\Python\dop\text\red_text.py
