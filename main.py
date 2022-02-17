import os
import random

RUSSIAN_ALPHABET = list(chr(i) for i in range(ord("а"), ord("я") + 1))
RUSSIAN_ALPHABET.append("ё")


class Character:
	def __init__(self, difficulty_level, game):
		self.hp = Character.get_hp_from_difficulty(difficulty_level)
		self.game = game
		self.name = self.choose_name()

	def choose_letter(self):
		raise Exception("Метод не был переопределён!")

	def choose_name(self):
		return Exception("Метод не был переопределён!")

	@staticmethod
	def get_hp_from_difficulty(difficulty_level):
		return {1: 20, 2: 15, 3: 10, 4: 5}[difficulty_level]


class Player(Character):
	def __init__(self, difficulty_level, game):
		super(Player, self).__init__(difficulty_level, game)

	def choose_letter(self):
		while True:
			letter = input("Введите букву: ").lower()
			if letter not in RUSSIAN_ALPHABET:
				print("Вы ввели символ, не входящий в русский алфавит. Попробуйте ещё раз.")
			else:
				break

		return letter

	def choose_name(self):
		return input("Введите имя: ")


class Bot(Character):
	i = 1

	def __init__(self, difficulty_level, game):
		super(Bot, self).__init__(difficulty_level, game)
		Bot.i += 1

	def choose_letter(self):
		return random.choice(self.game.letters)

	def choose_name(self):
		return f"Бот №{Bot.i}"


class Game:
	def __init__(self):
		self.difficulty_level = Game.choose_difficulty()

		self.players_list = list()
		self.initialize_players()
		self.players_number = 0

		self.letters = RUSSIAN_ALPHABET.copy()
		self.used_letters = list()

		self.word = str()
		self.initialize_game()

	@staticmethod
	def choose_difficulty():
		while True:
			level = int(input("Выберите уровень сложности:"
							  f"\n1 - игрок имеет {Character.get_hp_from_difficulty(1)} HP;"
							  f"\n2 - игрок имеет {Character.get_hp_from_difficulty(2)} HP;"
							  f"\n3 - игрок имеет {Character.get_hp_from_difficulty(3)} HP;"
							  f"\n4 - игрок имеет {Character.get_hp_from_difficulty(4)} HP.\n"))
			if level not in (1, 2, 3, 4):
				print("Введемно недопустимое значение. Попробуйте ещё раз.")
			else:
				break

		return level

	def print_word(self):
		string = "["
		for letter in self.word:
			if letter in self.used_letters:
				string += " " + letter
			else:
				string += " _"
		string += " ]"
		print(string)

	def initialize_players(self):
		number = int(input("Введите количество игроков: "))
		for i in range(number):
			self.players_list.append(Player(self.difficulty_level, self))
		number = int(input("Введите количество ботов: "))
		for i in range(number):
			self.players_list.append(Bot(self.difficulty_level, self))

	def initialize_game(self):
		length = {1: 5, 2: 6, 3: 7, 4: 8}[self.difficulty_level]

		with open("C:/Matvey/Programm/Python/dop/text/text.txt", "r", encoding="utf-8") as file:
			words = file.read().split(chr(10))

		playable_words = list()
		for word in words:
			if len(word) == length:
				playable_words.append(word)

		self.word = random.choice(playable_words)

	def play_game(self):
		while True:
			player = self.players_list[self.players_number]
			if player.hp == 0:
				self.players_number = (self.players_number + 1) % len(self.players_list)
				continue

			os.system("cls")
			self.print_word()

			print("Оставшиеся буквы:")
			letters = ""
			for letter in self.letters:
				letters += letter + " "
			print(letters)

			print("Использованные буквы:")
			used_letters = ""
			for letter in self.used_letters:
				used_letters += letter + " "
			print(used_letters)

			print("Игроки и их здоровье:")
			for _player in self.players_list:
				print(f"{_player.name}: {_player.hp}")

			print(f"Сейчас ходит {player.name}")

			while True:
				letter = player.choose_letter()
				if letter in self.used_letters:
					print("Эта буква уже была использована. Введите другую.")
				else:
					break

			self.letters.remove(letter)
			self.used_letters.append(letter)

			count = 0
			for let in self.word:
				if let in self.used_letters:
					count += 1
			if count == len(self.word):
				os.system("cls")
				print(f"{player.name} победил! Загаданное слово: {self.word}.")
				break

			if letter not in self.word:
				player.hp -= 1

				count = 0
				for player in self.players_list:
					if player.hp == 0:
						count += 1
				if count == len(self.players_list):
					os.system("cls")
					print(f"Все игроки потерпели поражение. Загаданное слово: {self.word}.")
					break

				self.players_number = (self.players_number + 1) % len(self.players_list)


if __name__ == '__main__':
	new_game = Game()
	new_game.play_game()

# py C:\\Matvey\Programm\Python\dop\pole_chud\main.py
