import random


class Player(object):
	"""docstring for Player"""

	def __init__(self, number, master='PC', hp=10):
		self.number = number
		self.master = master
		self.hp = hp
		self.name = random.choice(quality_list) + ' ' + random.choice(name_list)
		self.luck = True


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


def player_choice_let():
	global none_use_alph
	let = input('Какая буква?\n')
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
	if let not in word:
		player.hp -= 1
		player.luck = False


def print_word(what_print):
	print('[' + ''.join(what_print) + ']')


def print_alph(what_print):
	pr = ''
	for i in range(len(what_print)):
		pr += what_print[i] + ' '
	print(pr)


def screen(moover):
	print_word(pr_word)
	print_alph(alph)
	print(f'Ход {moover.name}, его HP = {moover.hp}')


def game():
	while True:
		for player_name in ("player_one", "player_two", 'player_three', 'player_four'):
			player = globals()[player_name]
			while player.luck == True:
				screen(player)
				if player.hp != 0:
					if player.master == "man":
						let = player_choice_let()
					else:
						let = comp_choice_let()

					finde(let, player)

					if ''.join(pr_word) == word:
						print('Выиграл ' + player.name)
						quit()
			player.luck = True



with open("C:/Matvey/Programm/Python/dop/text/text.txt", encoding='utf-8') as file:
	word_list = [row.strip() for row in file]
# word_list = ['слово', 'влад', 'автомобиль']

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
		'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

none_use_alph = alph

word = random.choice(word_list)
pr_word = ['#' for i in range(len(word))]

quality_list = ['Спящий', 'Под камнем лежащий']
name_list = ['Иигорь', 'Андрей']


def init_players():
	global player_one, player_two, player_three, player_four
	how_players = int(input('Сколько игроков? /Цифра от 0 до 4х/ \n'))
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


# py C:\\Matvey\Programm\Python\dop\pole_chud\pole_chudes.py
