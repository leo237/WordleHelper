import os
from collections import defaultdict

PROCESSED_FILE = os.path.join(os.getcwd(), 'processed_words.txt')
WORDS_FILE = os.path.join(os.getcwd(), 'words.txt')

NUMBER_OF_LETTERS = 5

def get_words(data_file_path=WORDS_FILE):
	with open(data_file_path) as dfp:
		words = set()
		for line in dfp:
			words.add(line)

	return words

def is_valid_n_letter_word(word, n):
	if len(word) == n and word.isalpha():
		return True
	return False

def pre_process(processed_file = PROCESSED_FILE, n = NUMBER_OF_LETTERS):
	if os.path.exists(processed_file):
		return
	words = get_words()
	n_letter_words = {word.strip().lower() for word in words if is_valid_n_letter_word(word.strip(), n)}

	char_sets = defaultdict(set)

	for word in n_letter_words:
		for char in word:
			char_sets[char].add(word)

	return char_sets

def find_words(char_sets, include, exclude, green_letters):
	
	potential_words = set()
	if len(include) >= 1:
		potential_words = char_sets[include[0]]
	else:
		for char in char_sets:
			potential_words.update(char_sets[char])

	for char in include:
		potential_words = potential_words.intersection(char_sets[char])

	for char in exclude:
		potential_words = potential_words.difference(char_sets[char])


	for green_letter in green_letters:
		idx = int(green_letter[0])
		char = green_letter[1]

		potential_words = {word for word in potential_words if word[idx] == char}


	print(potential_words)

	
def driver(char_sets):

	try_again = 'Y'
	included = []
	excluded = []
	found_green = []
	
	while(try_again.lower() != 'n'):
		include = input("Enter new letters to include without spaces (include green). [Already included : {}] [E.g. -- ro] : ".format(included))
		exclude = input("enter letters to exclude without spaces.[Already excluded : {}] [E.g. xy] : ".format(excluded))

		green_letters = input("enter idx and letters found. space separated. Start with 0. [Already found : {}] [E.g. 0r 1o 2b for rob__] :".format(found_green))

		if include:
			included.extend(list(include.strip()))
		if exclude:
			excluded.extend(exclude.strip())
		if green_letters:
			print(green_letters)
			found_green.extend(green_letters.split(' '))

		find_words(char_sets, included, excluded, found_green)

		try_again = input("Continue playing? y/n : ")


def main():
	char_sets = pre_process()
	driver(char_sets)


if __name__ == '__main__':
	main()