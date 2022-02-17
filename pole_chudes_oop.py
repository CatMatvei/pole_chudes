import random
import os
from time import sleep

RUS_ALPH = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
			'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']



class Character:
	def __init__(self, difficulty_level, game):
		self.hp = Character.get_hp(difficulty_level)
		self.game = game
		self.name = random.choice(QUALITY_LIST).capitalize() + ' ' + random.choice(NAME_LIST)
		self.luck = True
		self.points = 0

	def choice_letter(self, letter):
		self.game.none_use_alph.remove(letter)
		self.game.use_alph.append(letter)
		return letter

	@staticmethod
	def get_hp(difficulty_level):
		return {1: 20, 2: 15, 3: 10, 4: 5}[difficulty_level]


class Player(Character):
	def __init__(self, difficulty_level, game):
		super(Player, self).__init__(difficulty_level, game)

	def choice_letter(self):
		letter = input("Введите букву: ").lower()
		if letter not in RUS_ALPH:
			print('Чё не по русски базаришь?, минус 1 HP и кошка-жена')
		elif letter in self.game.use_alph:
			print(
				'Буква уже использована. Партия недовольна вами, минус 1 HP и миска риса')
			letter = '!'
		else:
			super().choice_letter(letter)
		return letter


class Bot(Character):
	def __init__(self, difficulty_level, game):
		super(Bot, self).__init__(difficulty_level, game)

	def choice_letter(self):
		letter = random.choice(self.game.none_use_alph)
		super().choice_letter(letter)
		return letter


class Screen:
	def start_menu():
		print('Поле чудес')
		return


	# Screen.play_menu(self, print_word(pr_word), print_alph(none_use_alph), print_alph(use_alph), player) 
	def play_menu(game, pr_word, none_use_alph, use_alph, player): 					
	# 	print(f'''
	# |*******************************************************************|
	# |						Pole Chudes									|
	# |Неизвестное слово: {pr_word}, количество букв: {game.len(word)}	|
	# |																	|
	# |  Оставшиеся буквы: 												|
	# | {none_use_alph} |
	# |  Использованные буквы:											|
	# | {use_alph} |
	# |-------------------------------------------------------------------|
	# |		Ходит {player.name}, его HP = {player.hp}, его очки = {player.points} 					|
	# |-------------------------------------------------------------------|
	# |					Якубович.пнг	Буква? 			 				|
	# | девки.джпг 					огурчики.гиф 	 ааавтомобиль.свг	|
	# |																	|
	# |===================================================================|
	# 			''')
		print(f'Неизвестное слово: {pr_word}, количество букв: {len(game.word)}')
		print(f'{none_use_alph}')
		print(f'{use_alph}')
		print(f'Ходит {player.name}, его HP = {player.hp}, его очки = {player.points}')
		return


	# Screen.final_menu(self.player_list, graveyard)
	def final_menu(player_list, graveyard):
		print(f'''
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@//\\\\						 //\\\\@@@@@
	@@@@//	\\\\			 			//	\\\\@@@@
	@@@//	 \\\\ 	   //\\\\ 	   //	 \\\\@@@
	@@// 	  \\\\	  //  \\\\	  // 	  \\\\@@
	@//			\\\\====//	   \\\\====/ 	   	   \\\\@
	//|+++++++==========/\\==========+++++++|\\\\ 	
	/| 				Pole Chudes 			|\\
	||				Результаты: 			||
					''')
		i = 0
		for player in player_list:
			i += 1
			print(f'|| №{i}: {player.name}, НР = {player.hp}, Очки = {player.points} 		||')
		print(f'||Умерло {graveyard} игроков||')
		print('''
	\\|										|/
	\\\\_____________________________________//
					''')
		time.sleep(4)
		return

		
class Game:
	def __init__(self):
		self.difficulty_level = Game.hard_mode()

		self.player_list = list()
		self.initialize_players()
		self.graveyard = 0
		# self.player_number = 0

		self.none_use_alph = RUS_ALPH.copy()
		self.use_alph = list()

		self.word = str()
		self.initialize_game()

	@staticmethod
	def hard_mode():
		while True:
			try:
				level = int(input("Выберите уровень сложности:"
								  	f"\n1 - игрок имеет {Character.get_hp(1)} HP;"
									f"\n2 - игрок имеет {Character.get_hp(2)} HP;"
									f"\n3 - игрок имеет {Character.get_hp(3)} HP;"
									f"\n4 - игрок имеет {Character.get_hp(4)} HP.\n"))
			except BaseException:
				print('мнх')
			else:
				if level in (1, 2, 3, 4):
					break
		return level


	def print_word(self, word):
		string = "["
		for letter in word:
			string += " " + letter
		string += " ]"
		return string

	def print_alph(self, alph):
		print_alph = ''
		for letter in alph:
			print_alph += letter + ' '
		return print_alph

	def initialize_players(self):
		num = int(input('Введите количество игроков: '))
		for i in range(num):
			self.player_list.append(Player(self.difficulty_level, self))
		num = int(input('Введите количество ботов: '))
		for i in range(num):
			self.player_list.append(Bot(self.difficulty_level, self))

	def initialize_game(self):
		
		self.word = random.choice(WORD_LIST)
		self.pr_word = ['#' for i in range(len(self.word))]

		self.none_use_alph = RUS_ALPH.copy()
		self.use_alph = list()


	def play(self):
		Screen.start_menu()
		while True:
			for player in self.player_list:
				while player.luck == True:
					Screen.play_menu(self, self.print_word(self.pr_word), self.print_alph(self.none_use_alph), self.print_alph(self.use_alph), player)
					letter = player.choice_letter()
					for i in range(len(self.word)):
						if letter == self.word[i]:
							self.pr_word[i] = letter
							player.points += 1
					if letter not in self.word:
						player.hp -= 1
						player.luck = False
					break
				player.luck = True

def download_fiels():
	with open("C:/Matvey/Programm/Python/dop/text/russian_nouns.txt", encoding='utf-8') as file:
		WORD_LIST = [row.strip() for row in file]

	with open("C:/Matvey/Programm/Python/dop/text/russian_pril.txt", encoding='utf-8') as file:
		QUALITY_LIST = [row.strip() for row in file]

	with open("C:/Matvey/Programm/Python/dop/text/russian_imena.txt", encoding='utf-8') as file:
		NAME_LIST = [row.strip() for row in file]
	return WORD_LIST, QUALITY_LIST, NAME_LIST


WORD_LIST, QUALITY_LIST, NAME_LIST = download_fiels()

new_game = Game()
new_game.play()


'''

def finde(let, player):
	zamena_alph(let)
	for i in range(len(word)):
		if let == word[i]:
			pr_word[i] = let
			player.points += 1
	if let not in word:
		player.hp -= 1
		player.luck = False


def screen(moover):
	# sleep(3)
	os.system('cls')
	print_word(pr_word)
	print_alph(alph)
	print(f'Ход {moover.name}, его HP = {moover.hp}')


def game():
	graveyard = 0
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






init_players()
game()

print('Слово: ', word)
print("Рейтинг:\n"
	f"\n Игрок {player_one.name} заработал {player_one.points} очков"
	f"\n Игрок {player_two.name} заработал {player_two.points} очков"
	f"\n Игрок {player_three.name} заработал {player_three.points} очков"
	f"\n Игрок {player_four.name} заработал {player_four.points} очков")
'''


# py C:\\Matvey\Programm\Python\dop\pole_chud\pole_chudes_oop.py
