###########################################################
# Computer Project #9
# Algorithm
# Open user entered file
# Obtain a set of words in the file by calling read_file function
# Obtain a dictionary of word completions by calling fill_completions function
# Prompt user to enter a prefix
# Find all word completions by calling find_completions function
# Sort the completed words alphabetically
# Display all the completed words if there are any
# If there are none, display message
# Repeatedly prompt for prefix until user enters '#'
# Quit the program
# Display closing message
###########################################################

import string


def open_file():
    '''
    Repeatedly prompts for a filename until the file is opened successfully
    Use an exception handler to consider invalid filenames
    Returns: file pointer
    '''

    file_name = input("\nInput a file name: ")

    # Repeatedly prompt for filename until a valid one is entered
    while True:
        try:
            # Try to open file for reading
            fp = open(file_name, 'r', encoding='UTF-8')

            # Return file pointer
            return fp
        # Exception handler to except invalid filename
        except IOError:
            print("\n[Error]: no such file")
            file_name = input("\nInput a file name: ")


def read_file(fp):
    '''
    Iterate through text file
    Create a list of all words in the file
    Iterate through words in the list
    Add the word without punctuation and whitespace to a new list
    Iterate through words in new list
    Check if the word is all alphabetic characters and greater than length 1
    If True, add word to return list
    Otherwise, continue to next word
    Create a set of the return list
    fp: text file pointer
    Returns: set of words
    '''

    my_list = []

    # Iterate through text file
    for line in fp:

        # Create a list of all words in the file
        lst = line.split()

        # Iterate through words in the list
        for val in lst:

            # Add the word without punctuation and whitespace to a new list
            my_list.append(val.strip().strip(string.punctuation).lower())
    new_lst = []

    # Iterate through words in new list
    for word in my_list:

        # Check if word is alphabetic characters and greater than length 1
        if not(word.isalpha() and (len(word) > 1)):
            continue
        else:
            new_lst.append(word)

    # Only keep unique words by creating a set
    word_set = set(new_lst)

    return word_set


def fill_completions(words):
    '''
    Iterate through every word in the words set
    Iterate through every character in the word, keeping track of index
    Check if the index and character is not already in dictionary keys
    If True, create new entry in dictionary with tuple of index and
    character as keys, and set of word as values
    Otherwise, add the word to existing key value pair values
    words: set of words
    Returns: dictionary 
    '''
    my_dict = {}

    # Iterate through every word in the words set
    for word in words:

        # Iterate through every character in the word, keeping track of index
        for i, ch in enumerate(word):

            # Check if key exists in dictionary
            if (((i, ch))) not in my_dict.keys():

                # Create new dictionary entry
                my_dict[(((i, ch)))] = {word}
            else:

                # Add word to existing key value pair
                my_dict[(((i, ch)))].add(word)

    return my_dict


def find_completions(prefix, word_dic):
    '''
    Initialize empty set
    If user entered prefix is empty, return empty set
    Otherwise, iterate through key value pairs in dictionary
    Iterate through every word in the values
    Check if the word starts with the user entered prefix
    If True, add word to set
    Otherwise, continue checking other words
    prefix: user entered prefix (string)
    word_dic: dictionary 
    Returns: set of words
    '''

    my_set = set()

    # Check if prefix is empty
    if prefix == '':
        return my_set
    else:

        # Iterate through key value pairs in dictionary
        for key, values in word_dic.items():

            # Iterate through every word in the values
            for value in values:

                # Check if the word starts with the user entered prefix
                if value.startswith(prefix):

                    # Add word to set of words
                    my_set.add(value)
                else:
                    continue

    return my_set


def main():
    '''
    Open user entered file
    Obtain a set of words in the file by calling read_file function
    Obtain dictionary of word completions by calling fill_completions 
    Prompt user to enter a prefix
    Find all word completions by calling find_completions function
    Sort the completed words alphabetically
    Display all the completed words if there are any
    If there are none, display message
    Repeatedly prompt for prefix until user enters '#'
    Quit the program
    Display closing message
    '''

    # Open user entered file
    fp = open_file()

    # Obtain a set of words in the file by calling read_file function
    set_of_words = read_file(fp)

    # Obtain dictionary of word completions by calling fill_completions
    completions = fill_completions(set_of_words)

    # Prompt user to enter a prefix
    prefix = input("\nEnter a prefix (# to quit): ")

    # Find all word completions by calling find_completions function
    words = find_completions(prefix, completions)

    # Sort the completed words alphabetically
    words = sorted(words)

    # Prompt for prefix input until input is '#'
    while prefix != '#':

        # Check if words set is not empty
        if len(words) > 0:

            # Display all words
            print("\nThe words that completes {} are: {}".format(
                prefix, ', '.join(words)))
        else:
            # Display message that there are no completions
            print("\nThere are no completions.")

        prefix = input("\nEnter a prefix (# to quit): ")
        words = find_completions(prefix, completions)
        words = sorted(words)

    print("\nBye")


if __name__ == '__main__':
    main()
