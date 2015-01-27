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
        line = each_line.strip()
        words = line.split(" ")
        for word in words:
            word = word.lower()
            chaining_list.append(word)

    # loops through the words in the list
    

    # until the 3-last word in the list is reached, creates keys in the dictionary as tuples of the word it is on and the word following; 
    #     with the word after that as the key
    # if the tuple is already in the dictionary, it overwrites the existing value and adds the word that it hasn't already counted

    for x in range(0,(len(chaining_list)-2)):
        tuple_key = (chaining_list[x], chaining_list[x + 1])
        if tuple_key not in chaining_dict:
            chaining_dict[tuple_key] = [chaining_list[x + 2]]
        else:
            chaining_dict[tuple_key] = chaining_dict[tuple_key] + [chaining_list[x + 2]]

        # word_index = chaining_list.index(x)
        # word_index = chaining_list.index(x)
        # tuple_key = (chaining_list[word_index], chaining_list[word_index + 1])

        # if tuple_key not in chaining_dict:
        #     chaining_dict[tuple_key] = [chaining_list[word_index + 2]]

        # else:
        #     chaining_dict[tuple_key] = chaining_dict[tuple_key] + [chaining_list[word_index + 2]]
        # chaining_dict[tuple_key] = chaining_dict.get(tuple_key, []) + [chaining_list[word_index + 2]]

    print chaining_dict
    return chaining_dict


def make_text(chains):
    """Creates random text based on the original text(s) from the dictionary created above"""
    # will append the randomly selected text into a list that will eventually become our message
    current_key = random.choice(chains.keys())
    text_list = current_key[0] + " " + current_key[1]
    

    while current_key in chains:
        next_word = random.choice(chains[current_key])
        text_list = text_list + " " + next_word
        current_key = (current_key[-1], next_word)

    print text_list
    return text_list


def main():
    args = sys.argv

    # Change this to read input_text from a file
    original_text = "dr dreuss.txt"

    chain_dict = make_chains(original_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()