import random
import os
from time import sleep

RUS_ALPH = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
			'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


# Класс всех персонажей (игроков и ботов)
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


# Класс игроков. 
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


# Класс ботов.
class Bot(Character):
	def __init__(self, difficulty_level, game):
		super(Bot, self).__init__(difficulty_level, game)

	def choice_letter(self):
		letter = random.choice(self.game.none_use_alph)
		super().choice_letter(letter)
		return letter


# Класс экрана, используется как хранилище функций.
class Screen:
	def start_menu():
		print('Поле чудес')
		return


	# Screen.play_menu(self, print_word(pr_word), print_alph(none_use_alph), print_alph(use_alph), player) 
	def play_menu(game, pr_word, none_use_alph, use_alph, player): 		
		os.system('cls')			
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


	# Screen.final_menu(self, self.player_list, graveyard)
	def final_menu(game, player_list, graveyard):
		os.system('cls')
		print(f'''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@//\\\\                      //\\\\@@@@@
@@@@//  \\\\                    //  \\\\@@@@
@@@//	 \\\\ 	   //\\\\ 	   //	 \\\\@@@
@@// 	  \\\\	  //  \\\\	  // 	  \\\\@@
@//			\\\\====// \\\\====/   	   \\\\@
//|+++++++==========/\\==========+++++++|\\\\ 	
/| 				Pole Chudes 			|\\
||				Результаты: 			||
					''')
		i = 0
		for player in player_list:
			i += 1
			print(f'|| №{i}: {player.name}, НР = {player.hp}, Очки = {player.points} 		||')
		print(f'||Умерло {graveyard} игроков||')
		print(f'Слово: {game.word}')
		print('''
\\|					|/
\\\\_____________________________________//
					''')
		sleep(4)
		return


	def died_photo(player):
		print(f'Игрок {player.name} умер. Ход переходит следующему игроку.')
		return

		
# Главный класс игры.
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
		while self.graveyard != len(self.player_list) and self.word != ''.join(self.pr_word):
			for player in self.player_list:
				while player.luck == True and self.graveyard != len(self.player_list) and player.hp != 0:
					Screen.play_menu(self, self.print_word(self.pr_word), self.print_alph(self.none_use_alph), self.print_alph(self.use_alph), player)
					letter = player.choice_letter()
					
					for i in range(len(self.word)):
						if letter == self.word[i]:
							self.pr_word[i] = letter
							player.points += 1
					
					if letter not in self.word:
						player.hp -= 1
						player.luck = False
						if player.hp == 0:
							self.graveyard += 1
							Screen.died_photo(player)

					if self.word == ''.join(self.pr_word):
						Screen.final_menu(self, self.player_list, self.graveyard)
						return
					
				player.luck = True

		if self.graveyard == len(self.player_list):
			Screen.final_menu(self, self.player_list, self.graveyard)
			return


# Функция подключения файлов, поставить свой путь. Существительные, прилагательные, имена. 
# def download_fiels():
# 	# C:\Matvey\Programm\Python\dop\pole_chud\wordbooks
# 	with  open(os.path.dirname(os.path.abspath(__file__)) + "/wordbooks/russian_nouns.txt", encoding='utf-8') as file:
# 		WORD_LIST = [row.strip() for row in file]

# 	with open(os.path.dirname(os.path.abspath(__file__)) + "/wordbooks/russian_pril.txt", encoding='utf-8') as file:
# 		QUALITY_LIST = [row.strip() for row in file]

# 	with open(os.path.dirname(os.path.abspath(__file__)) + "/wordbooks/russian_imena.txt", encoding='utf-8') as file:
# 		NAME_LIST = [row.strip() for row in file]
# 	return WORD_LIST, QUALITY_LIST, NAME_LIST

def download_fiels():
	basedir = os.path.abspath(os.getcwd())
	wordbooks_dir = os.path.abspath(os.path.join(basedir, '..'))
	# C:\Matvey\Programm\Python\dop\pole_chud\wordbooks
	with  open(os.path.join(wordbooks_dir, '/russian_nouns.txt'), encoding='utf-8') as file:
		WORD_LIST = [row.strip() for row in file]

	with open(os.path.dirname(os.path.abspath(__file__)) + "/wordbooks/russian_pril.txt", encoding='utf-8') as file:
		QUALITY_LIST = [row.strip() for row in file]

	with open(os.path.dirname(os.path.abspath(__file__)) + "/wordbooks/russian_imena.txt", encoding='utf-8') as file:
		NAME_LIST = [row.strip() for row in file]
	return WORD_LIST, QUALITY_LIST, NAME_LIST


WORD_LIST, QUALITY_LIST, NAME_LIST = download_fiels()

new_game = Game()
new_game.play()


# py C:\\Matvey\Programm\Python\dop\pole_chud\pole_chudes_oop.py
