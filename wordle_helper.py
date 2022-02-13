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

def find_words(char_sets, include, exclude, green_letters, yellow_letters):
	
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

	for yellow_letter in yellow_letters:
		idx = int(yellow_letter[0])
		char = yellow_letter[1]

		potential_words = {word for word in potential_words if word[idx] != char}


	print(potential_words)


def run_driver(char_sets):
	try_again = 'Y'
	included = []
	excluded = []
	found_green = []
	found_yellow = []

	while(try_again.lower() != 'n'):
		word_entered = input("Enter word you entered : ")
		colors = input("Enter the colors for each letter. Use key (x) for grey, (y) for yellow and (g) for green. No spaces e.g. xyxxgx :")
		
		# Sanity
		if len(word_entered) != len(colors):
			print("Sorry, the number of characters did not match. Try again")
			continue

		for idx in range(len(word_entered)):
			if colors[idx].lower() == 'x':
				excluded.append(word_entered[idx])
			elif colors[idx].lower() == 'y':
				found_yellow.append([idx, word_entered[idx]])
				included.append(word_entered[idx])
			elif colors[idx].lower() == 'g':
				found_green.append([idx, word_entered[idx]])
				included.append(word_entered[idx])

		find_words(char_sets, included, excluded, found_green, found_yellow)
		try_again = input("Continue playing? y/n : ")


def main():
	char_sets = pre_process()
	run_driver(char_sets)


if __name__ == '__main__':
	main()