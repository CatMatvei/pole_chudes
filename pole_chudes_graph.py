import random
import os
from time import sleep


class Player(object):
	"""docstring for Player"""

	def __init__(self, number, master='PC', hp=10):
		self.number = number
		self.master = master
		self.hp = hp
		self.name = random.choice(quality_list).capitalize(
		) + ' ' + random.choice(name_list)
		self.luck = True
		self.points = 0


def hard_mode():
	rang = {1: 5, 2: 10, 3: 15, 4: 500}
	try:
		k = int(
			input('Выбери уровень сложности цифрой: мастер/средний/новичок/нерожденный: '))
		ret = rang[k]
	except BaseException:
		print('мнх')
		quit()
	return ret


def choice_let(moover):
	if moover.master == "man":
		let = player_choice_let(input())
	else:
		let = comp_choice_let()
	return let


def player_choice_let(inp):
	global none_use_alph
	let = inp
	# let = input('Какая буква?\n')
	try:
		none_use_alph.remove(let)
	except ValueError:
		print('Буква уже использована. Партия недовольна вами, минус 1 HP и миска риса')
		let = '!'
	return let


def comp_choice_let():
	global none_use_alph
	let = random.choice(none_use_alph)
	none_use_alph.remove(let)
	return let


def zamena_alph(let):
	for i in range(len(alph)):
		if alph[i] == let:
			alph[i] = '_'


def finde(let, player):
	zamena_alph(let)
	for i in range(len(word)):
		if let == word[i]:
			pr_word[i] = let
			player.points += 1
	if let not in word:
		player.hp -= 1
		player.luck = False


def print_word(what_print):
	# print('[' + ''.join(what_print) + ']')
	return ('[' + ''.join(what_print) + ']')


def print_alph(what_print):
	pr = ''
	for i in range(len(what_print)):
		pr += what_print[i] + ' '
	# print(pr)
	return pr


def screen(moover):
	# sleep(3)
	# os.system('cls')
	print(f'''
|*******************************************************************|
|                       Pole Chudes                                 |
|Неизвестное слово: {print_word(pr_word)}, количество букв: {len(word)}|
|                                                                   |
|  Оставшиеся буквы:                                                |
| {print_alph(alph)}                                                |
|-------------------------------------------------------------------|
|Ходит {moover.name}, его HP = {moover.hp}, его очки = {moover.points}|
|-------------------------------------------------------------------|
|					Якубович.пнг	Буква? 	буква	|
| девки.джпг 					огурчики.гиф 	 ааавтомобиль.свг	|
|																	|
|===================================================================|
''')
	# print_word(pr_word)
	# print_alph(alph)
	# print(f'Ход {moover.name}, его HP = {moover.hp}')


def game():
	graveyard = 0
	while True:
		for player_name in ("player_one", "player_two", 'player_three', 'player_four'):
			player = globals()[player_name]
			while player.luck == True:
				screen(player)
				if player.hp != 0:
					let = choice_let(player)

					finde(let, player)

					if player.hp == 0:
						print('YOU DIED')
						graveyard += 1
						if graveyard == 4:
							print('Победа. Смерть всех.')
							quit()

					if ''.join(pr_word) == word:
						print('Выиграл ' + player.name)
						return
			player.luck = True


with open("C:/Matvey/Programm/Python/dop/text/russian_nouns.txt", encoding='utf-8') as file:
	word_list = [row.strip() for row in file]
# word_list = ['слово', 'влад', 'автомобиль']

with open("C:/Matvey/Programm/Python/dop/text/russian_pril.txt", encoding='utf-8') as file:
	quality_list = [row.strip() for row in file]
# quality_list = ['Спящий', 'Под камнем лежащий']

with open("C:/Matvey/Programm/Python/dop/text/russian_imena.txt", encoding='utf-8') as file:
	name_list = [row.strip() for row in file]
# name_list = ['Иигорь', 'Андрей']

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
		'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

none_use_alph = alph

word = random.choice(word_list)
pr_word = ['#' for i in range(len(word))]


def init_players():
	global player_one, player_two, player_three, player_four
	how_players = int(input('Сколько игроков? /Цифра от 0 до 4х/? \n'))
	for i in range(how_players):
		if i == 0:
			player_one = Player(1, 'man', hard_mode())
		elif i == 1:
			player_two = Player(2, 'man', hard_mode())
		elif i == 2:
			player_three = Player(3, 'man', hard_mode())
		elif i == 3:
			player_four = Player(4, 'man', hard_mode())
		else:
			print('мнх')
			quit()

	for i in range(4 - how_players):
		if i == 0:
			player_four = Player(4)
		elif i == 1:
			player_three = Player(3)
		elif i == 2:
			player_two = Player(2)
		elif i == 3:
			player_one = Player(1)
		else:
			print('мнх')
			quit()


init_players()
game()

print('Слово: ', word)
print("Рейтинг:\n"
	  f"\n Игрок {player_one.name} заработал {player_one.points} очков"
	  f"\n Игрок {player_two.name} заработал {player_two.points} очков"
	  f"\n Игрок {player_three.name} заработал {player_three.points} очков"
	  f"\n Игрок {player_four.name} заработал {player_four.points} очков")


# py C:\Matvey\Programm\Python\dop\pole_chud\pole_chudes_graph.py
