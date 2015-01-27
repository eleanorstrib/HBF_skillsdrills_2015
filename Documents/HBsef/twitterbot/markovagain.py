
import random

TWITTER_CHARACTER_MAX = 139


def make_chains(corpus):
	original_file = open(corpus)

	chaining_list = []
	chaining_dict = {}

	for each_line in original_file:
		line = each_line.strip()
		word = line.split(" ")
		word = [words.lower() for words in word]
		chaining_list.extend(word)


	for w_index in range(0, len(chaining_list) - 2):
		key_tuple = (chaining_list[w_index], chaining_list[w_index + 1])
		chaining_dict[key_tuple] = chaining_dict.get(key_tuple, []) + [chaining_list[w_index + 2]]

	# Add a period at the end of the sentence

	return chaining_dict


def make_text(chaining):
	# text_list = []
	text_string = ""

	random_key = random.choice(chaining.keys())
	text_string = random_key[0] + " " + random_key[1]

	while random_key in chaining and len(text_string) <= 139:
		next_word = random.choice(chaining[random_key])
		text_string = text_string + " " + next_word
		random_key = (random_key[-1], next_word)

	return text_string

def main():
	original_data = ("wildedickens.txt")
	create_dictionary = make_chains(original_data)
	generate_tweet = make_text (create_dictionary)

	print generate_tweet


main()