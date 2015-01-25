#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chaining_list = []

    chaining_dict = {}

    original_text = open(corpus)

    # format the original text as one giant list, removing carriage returns, spaces and putting everything in lower case

    for each_line in original_text:
        line = each_line.strip("\n")
        words = line.split(" ")
        words = [item.lower() for item in words]
        chaining_list.extend(words)

    # loops through the words in the list
    for word in chaining_list:
        word_index = chaining_list.index(word)
        # until the 3-last word in the list is reached, creates keys in the dictionary as tuples of the word it is on and the word following; 
        #     with the word after that as the key
        # if the tuple is already in the dictionary, it overwrites the existing value and adds the word that it hasn't already counted
        if word_index in range(0,(len(chaining_list)-2)):
            tuple_key = (chaining_list[word_index], chaining_list[word_index + 1])
            chaining_dict[tuple_key] = chaining_dict.get(tuple_key, []) + [chaining_list[word_index + 2]]

    return chaining_dict
#FIXME -- remove test text
# make_chains('green.txt')

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""


#     return "Here's some random text."


# def main():
#     args = sys.argv

#     # Change this to read input_text from a file
#     input_text = "Some text"

#     chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

# if __name__ == "__main__":
#     main()
