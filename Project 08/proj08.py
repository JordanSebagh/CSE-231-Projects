#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:42:31 2023

@author: jordansebagh
"""

###########################################################
# Computer Project #8
# Algorithm 
# Prompt user to enter games file
# Prompt user to enter discount file
# Display menu of options
# Prompt user to enter menu option
# Display error message if menu option is invalid
# If the option is 1:
#    Prompt the user to enter a year
#    If the year is not an integer, display error message and reprompt
#    Get all games released during input year
#    Display games if there are any
#    Otherwise, display message that there are no games
# If option is 2:
#    Prompt for developer input
#    Display games released by developer if there are any
#    Otherwise, display message that there are no games
# If option is 3:
#    Prompt user for genre input
#    Display games in genre if there are any
#    Otherwise, display message that there are no games
# If option is 4:
#    Prompt user for developer and year input
#    If the year is not an integer, display error message and reprompt
#    Display games released during input year and by developer
#    If there are no games, display message that there are no games
# If option is 5:
#    Prompt for genre input
#    Display games in genre that do not offer discounts
#    If there are no games, display message that there are no games
# If option is 6:
#    Prompt for developer input
#    Display games by developer and do not offer discounts
#    If there are no games, display message that there are no games
# If option is 7:
#    Quit program
# Display closing message
###########################################################

import csv
from operator import itemgetter


MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''
        
      
        
def open_file(s):
    '''
    Repeatedly prompts for a filename until the file is opened successfully
    Use an exception handler to consider invalid filenames
    s: string
    Return file pointer
    '''
    
    # Prompt for file name
    filename = input('\nEnter {} file: '.format(s))
    
    # Loop until valid file has been entered
    while True:

        try:
            # Open file
            fp = open(filename, 'r', encoding='utf-8')
            return fp
        
        except IOError:
            print('\nNo Such file')
            filename = input('\nEnter {} file: '.format(s))
            
        

def read_file(fp_games):
    '''
    Skip header row of file
    Iterate through lines in file
    Get date, dev, genre, game mode, price, review, percent pos, and support
    Append all values to a list
    Create a dictionary with the game name as key, and info as values
    fp_games: games file pointer
    Returns: dictionary
    '''
    my_dict = {}
    
    csv_reader = csv.reader(fp_games)
    # Skip header row
    next(csv_reader)
    
    # Iterate through file
    for line in csv_reader:
        my_list = []
        
        # Obtain date
        date = line[1]
        my_list.append(date)
        
        # Obtain developer
        developer = line[2].split(';')
        my_list.append(developer)
        
        # Obtain genre
        genre = line[3].split(';')
        my_list.append(genre)
        
        # Obtain mode
        mode_name = line[4][0]
        if mode_name == 'M':
            mode = 0
        else:
            mode = 1
        my_list.append(mode)
        
        try:
            # Get the price in dollars
            price = line[5]
            price = price.replace(',', '')
            price = float(price)
            price = price * 0.012
            my_list.append(price)
            
        except ValueError:
            price = 0.0
            
            
            my_list.append(price)
        
        # Obtain overall reviews
        overall_review = line[6]
        my_list.append(overall_review)
        
        # Obtain reviews
        reviews = int(line[7])
        my_list.append(reviews)
        
        # Get percent positive value
        percent_positive = line[8].replace('%', '')
        percent_positive = int(percent_positive)
        
        my_list.append(percent_positive)
        
        support = []
        
        # Determine support value
        if line[9] == '1':
            support.append('win_support')
        if line[10] == '1':
            support.append('mac_support')
        if line[11] == '1':
            support.append('lin_support')
        
        my_list.append(support)
        
        # Create dictionary with game name as key and list of info as values
        my_dict[line[0]] = my_list
        
    return my_dict
        


def read_discount(fp_discount):
    '''
    Skip header row of discount file
    Iterate through discount file lines
    Round the discount value to 2 decimal places
    Create dictionary with the name of the game as key and discount as value
    fp_discount: discount file pointer
    Returns: Dictionary
    '''
    
    my_dict = {}
    
    csv_reader = csv.reader(fp_discount)
    # Skip header row
    next(csv_reader)
    
    # Iterate through file
    for line in csv_reader:
        # Get discount value
        value = float(line[1])
        # Round discount value 
        value = round(value, 2)
        # Add key and values to dictionary
        my_dict[line[0]] = value
    
    return my_dict
    
    
    
    
    
    
    
    


def in_year(master_D,year):
    '''
    Iterate through key value pairs in dictionary
    Obtain the year by using string slicing
    Check if year matches input year
    If True, add the game name to a list
    Sort the list alphabetically
    master_D: Main dictionary
    year: year of game release (int)
    Returns: sorted list of games
    '''
    my_list = []
    
    # Iterate through key value pairs
    for key, values in master_D.items():
        date = values[0]
        # Obtain the year of release
        line_year = date[-4:]
        
        # Check if year matches input year
        if int(line_year) == year:
            # Add game name to list
            my_list.append(key)
    
    my_list.sort()
    
    return my_list





def by_genre(master_D,genre): 
    '''
    Iterate through key value pairs
    Iterate through values in genre list
    Check if a genre matches input genre
    If True, add game name to list and percent positive reviews
    Iterate through every other value in list
    Add a tuple of game name and percent positive to new list
    Sort the new list based on percent positive in reverse order
    Extract the game name from the list and return a list of games
    master_D: Main dictionary
    genre: genre of game (string)
    Returns: sorted list of game names
    '''
    my_list = []
    
    # Iterate through key value pairs
    for key, values in master_D.items():
        
        # Iterate through values in genre list
        for item in values[2]:
            
            # Check if a genre matches input genre
            if item == genre:
                
                # Add game name and percent positive to list
                my_list.append(key)
      
                my_list.append(values[7])
    
    
    new_list = []
    # Iterate through every other value in list
    for i in range(0, len(my_list), 2):
        
        # Add a tuple of game name and percent positive to new list
        new_list.append(((my_list[i], my_list[i+1])))
    
    # Sort the new list based on percent positive in reverse order
    lst = sorted(new_list, key=itemgetter(1), reverse = True)
    
    return_lst = []
    
    # Extract the game name from the list
    for tup in lst:
        return_lst.append(tup[0])
        
    return return_lst
                            


        
def by_dev(master_D,developer): 
    '''
    Iterate through key value pairs in dictionary
    Iterate through developers inside dictionary
    Check if value in list is the same as input developer
    If True, add game name and release year to list 
    Iterate through values in list
    Create tuples of game name and release year and add to list
    Sort the list from latest to oldest games
    Extract game name from list of tuples
    master_D: Master dictionary
    developer: input game developer (string) 
    Returns: list of game names
    '''
    my_list = []
    
    # Iterate through key value pairs
    for key, values in master_D.items():
        # Iterate through values in list
        for item in values[1]:
            # Check if value is the same as developer parameter
            if item == developer:
                # Append key to list
                my_list.append(key)
                # Append release date to list
                my_list.append(values[0])
    
    new_list = []
    # Iterate through list 
    for i in range(0, len(my_list), 2):
        # Append a tuple of names and the year to a list
        new_list.append(((my_list[i], my_list[i+1][-4:])))
    
    # Sort the list from latest to oldest released games
    lst = sorted(new_list, key=itemgetter(1), reverse = True)
        
    return_lst = []
    
    # Append the name of game to return list 
    for tup in lst:
        return_lst.append(tup[0])
    
    return return_lst

    







def per_discount(master_D,games,discount_D): 
    '''
    Iterate through every game in input games list
    Iterate through key value pairs in dictionary
    Check if key and game are the same
    If True, append game name and price to list
    Iterate through discount dictionary key value pairs
    Check if the game name already exists in the list
    If True, calculate discount price and replace price with discount price
    Return price values
    master_D: Main dictionary
    games: list of game names
    discount_D: discount dictionary
    Returns: list of discounted prices
    '''
    
    my_list = []
    
    # Iterate through every game in input games list
    for game in games:
        
        # Iterate through key value pairs in dictionary
        for key, values in master_D.items():
            
            # Check if key and game are the same
            if key == game:
                
                # Add game name and price to list
                my_list.append(key)
                my_list.append(values[4])

    new_list = []

    # Iterate through discount dictionary key value pairs
    for key, values in discount_D.items():
        
        # Check if the game name already exists in the list
        if key in my_list:
            index = my_list.index(key)
            
            # Calculate discounted price
            new_value = 1 - (values/100)
            new_value = new_value * my_list[index + 1]
            
            # Replace price with discounted price
            my_list[index + 1] = round(new_value, 6)

    # Extract discounted price values
    return_lst = my_list[1::2]
    
    return return_lst
    

def by_dev_year(master_D,discount_D,developer,year):
    '''
    Iterate through key value pairs
    Extract year from release date
    Iterate through developer values
    Check if developer and year input match values in dictionary
    If True, add game name and price to list
    Iterate through key value pairs in discount dictionary
    Check if game name already exists in list
    If True, calculate discounted price and replace old value with discount
    Iterate through list of game names and prices
    Create tuples of each game and associated price
    Sort list of tuples by increasing prices
    Extract game name from sorted list
    master_D: Master dictionary
    discount_D: discount dictionary
    developer: game developer (string)
    year: release year (int)
    Returns: sorted list of games
    '''
    my_list = []
    
    # Iterate through key value pairs
    for key, values in master_D.items():
        
        # Extract year from release date
        current_year = values[0][-4:]

        # Iterate through developer values
        for item in values[1]:

            # Check if developer and year input match values in dictionary
            if int(current_year) == int(year) and developer == item:
                
                # Add game name and price to list
                my_list.append(key)
                my_list.append(values[4])
    
    # Iterate through key value pairs in discount dictionary
    for key, values in discount_D.items():
        
        # Check if game name already exists in list
        if key in my_list:
            index = my_list.index(key)
            new_value = values
            
            # Calculate discounted price
            percent = (100 - new_value) * 0.01

            new_value = my_list[index + 1] * percent
            
            # Replace old price with discount price
            my_list[index + 1] = new_value
    
            
    new_list = []
    
    # Iterate through list game names and prices
    for i in range(0, len(my_list), 2):
        
        # Create tuples of each game and associated price
        new_list.append(((my_list[i], my_list[i + 1])))
    
    # Sort list of tuples by increasing prices
    new_list = sorted(new_list, key=itemgetter(1))
    
    return_lst = []
    
    for tup in new_list:
        # Extract game name from sorted list
        return_lst.append(tup[0])
    
    return return_lst
    
   
def by_genre_no_disc(master_D,discount_D,genre):
    '''
    Iterate through key value pairs in dictionary
    Iterate through every genre in list of genres
    Check if genre matches input genre
    If True, add game name, price, and percent positive to list
    Iterate through discount dictionary key value pairs
    Check if game name already exists in list
    If True, delete the game name and associated price and percent positive
    Iterate through list and create tuples of game and associated values
    Sort the list first by price, then percent positive in reverse order
    Sort the list by price 
    Extract game name from sorted list
    master_D: Master dictionary
    discount_D: discount dictionary
    genre: genre of game (string)
    Returns: sorted list of games
    '''
    
    
    my_list = []
    
    # Iterate through key value pairs in dictionary
    for key, values in master_D.items():
        genres = values[2]
        
        # Iterate through every genre in list of genres
        for current_genre in genres:
            if current_genre == genre:
                
                # Add game name, price, and percent positive to list
                my_list.append(key)
                my_list.append(values[4])
                my_list.append(values[7])
    
    # Iterate through discount dictionary key value pairs
    for key, values in discount_D.items():
        
        # Check if game name already exists in list
        if key in my_list:
            index = my_list.index(key)
            
            # Delete game name and associated values from list
            del my_list[index]
            del my_list[index]
            del my_list[index]
    
    new_list = []
    
    # Iterate through list 
    for i in range(0, len(my_list), 3):
        
        # Create tuples of game and associated values
        new_list.append(((my_list[i], my_list[i + 1], my_list[i + 2])))
    
    # Sort the list first by price, then percent positive in reverse order
    new_list = sorted(new_list, key=itemgetter(1, 2), reverse = True)
    
    # Sort the list by price 
    new_list = sorted(new_list, key=itemgetter(1), reverse = False)
    
    
    
    return_lst = []
    
    
    for tup in new_list:
        # Extract game name from list of tuples
        return_lst.append(tup[0])
    
    return return_lst
            
    
    
    


def by_dev_with_disc(master_D,discount_D,developer):
    '''
    Iterate through key value pairs in dictionary
    Iterate through developers in developers list
    Check if input developer matches current developer
    If True, add game name to list
    Iterate through discount dictionary key value pairs
    Check if game name already exists in list
    If True, add a tuple of game name and discounted price to new list
    Sort new list by price 
    Extract game name from list of tuples
    master_D: Master dictionary
    discount_D: discount dictionary
    developer: game developer (string)
    Returns: sorted list of games 
    '''
    
    my_list = []
    
    # Iterate through key value pairs in dictionary
    for key, values in master_D.items():
        dev = values[1]
        
        # Iterate through developers in developers list
        for value in dev:
            
            # Check if input developer matches current developer
            if value == developer:
                
                # Add game name to list
                my_list.append(key)
    
    new_list = []
    
    # Iterate through discount dictionary key value pairs
    for key, values in discount_D.items():
        
        # Check if game name already exists in list
        if key in my_list:
            
            # Add a tuple of game name and discounted price to new list
            new_list.append(((key, values)))
    
    # Sort new list by price 
    new_list = sorted(new_list, key=itemgetter(1))
    
    return_lst = []
    
    # Extract game name from list of tuples
    for tup in new_list:
        return_lst.append(tup[0])
    
    return return_lst
        
       

        
def main():
    '''
    Open games file
    Open discount file
    Obtain discount dictionary by calling read_discount
    Prompt for option by displaying menu of options
    If the user selects option 1, prompt for year input
    Try converting year input to integer type
    Display error message if unsuccessful
    Obtain list of games in input year by calling in_year function
    Display all games if the list is not empty
    If the list is empty, print message
    If the user selects option 2, prompt for developer input
    Obtain list of games with developer by calling by_dev function
    Display all games if the list is not empty
    If the list is empty, print message
    If the user selects option 3, prompt for genre input
    Obtain list of games with genre by calling by_genre function
    Display all games if the list is not empty
    If the list is empty, print message
    If the user selects option 4, prompt for developer and year input
    Try converting year input to integer type
    Display error message if unsuccessful
    Obtain list of games with developer and year by calling by_dev_year
    Display all games if the list is not empty
    If the list is empty, print message
    If the user selects option 5, prompt for genre input
    Get list of games with genre and no discount by calling by_genre_no_disc
    Display all games if the list is not empty
    If the list is empty, print message
    If the user selects option 6, prompt for developer input
    Get list of games with developer and discounts by calling by_dev_with_disc
    Display all games if the list is not empty
    If the list is empty, print message
    If the user selects option 7, quit the program
    Display closing message
    '''
    
    # Open games file
    fp_games = open_file('games')
    
    # Open discount file
    fp_discount = open_file('discount')
    
    master_dictionary = read_file(fp_games)
    
    discount_dict = read_discount(fp_discount)
    
    
    
    
    option = input(MENU)
    
    option = int(option)
    
    # Check if option is within 1-7
    while option not in range(1,8):
        print("\nInvalid option")
        option = input(MENU)
        option = int(option)
        
    # Loop until user selects option 7
    while option != 7:
        
        if option == 1:
            year = input('\nWhich year: ')
            # Prompt for year input until converted to int type
            while True:
                try:
                    year = int(year)
                    
                    # Exit loop if converted to int type
                    break
                except ValueError:
                    # Display error message
                    print("\nPlease enter a valid year")
                    
                    # Reprompt for year input
                    year = input('\nWhich year: ')
                    
            year_list = in_year(master_dictionary, year)
            
            # Check if list is empty
            if len(year_list) != 0:
                # Display games separated by a comma and space
                print("\nGames released in {}:".format(year))
                print(', '.join(year_list))
            
            else:
                print("\nNothing to print")
            
            option = input(MENU)
            
            option = int(option)
            
            # Check if option input is within 1-7
            while option not in range(1,8):
                print("\nInvalid option")
                option = input(MENU)
                option = int(option)
                
        if option == 2:
            developer = input('\nWhich developer: ')
            
            developer_list = by_dev(master_dictionary, developer)
            
            # Check if list of games is empty
            if len(developer_list) != 0:
                print("\nGames made by {}:".format(developer))
                
                # Display games separated by a comma and space
                print(', '.join(developer_list))
            else:
                print("\nNothing to print")
            
            option = input(MENU)
            
            option = int(option)
            # Check if option input is within 1-7
            while option not in range(1,8):
                print("\nInvalid option")
                option = input(MENU)
                option = int(option)
        
        if option == 3:
            genre = input('\nWhich genre: ')
            genre_list = by_genre(master_dictionary, genre)
            
            # Check if list of games is empty
            if len(genre_list) != 0:
                print("\nGames with {} genre:".format(genre))
                
                # Display games separated by a comma and space
                print(', '.join(genre_list))
            else:
                print("\nNothing to print")
        
            option = input(MENU)
            
            option = int(option)
            
            # Check if option input is within 1-7
            while option not in range(1,8):
                print("\nInvalid option")
                option = input(MENU)
                option = int(option)
        
        if option == 4:
            dev = input('\nWhich developer: ')
            year = input('\nWhich year: ')
            
            # Prompt for year input until converted to int type
            while True:
                try:
                    year = int(year)
                    
                    # Exit loop if converted to int type
                    break
                except ValueError:
                    
                    # Display error message and reprompt 
                    print("\nPlease enter a valid year")
                    year = input('\nWhich year: ')
            
            dev_lst = by_dev_year(master_dictionary, discount_dict, dev, year)
            
            # Check if list of games is empty
            if len(dev_lst) != 0:
                print("\nGames made by {} and \
released in {}:".format(dev, year))
                
                # Display games separated by a comma and space
                print(', '.join(dev_lst))
            else:
                print("\nNothing to print")
            
            option = input(MENU)
            
            option = int(option)
            
            # Check if option input is within 1-7
            while option not in range(1,8):
                print("\nInvalid option")
                option = input(MENU)
                option = int(option)
        
        if option == 5:
            genre = input('\nWhich genre: ')
            gen_lst = by_genre_no_disc(master_dictionary,discount_dict,genre)
            
            # Check if list of games is empty
            if len(gen_lst) != 0:
                print("\nGames with {} genre and without a \
discount:".format(genre))
                
                # Display games separated by a comma and space
                print(', '.join(gen_lst))
            else:
                print("\nNothing to print")
            
            option = input(MENU)
            
            option = int(option)
            
            # Check if option input is within 1-7
            while option not in range(1,8):
                print("\nInvalid option")
                option = input(MENU)
                option = int(option)
        
        if option == 6:
            dev = input('\nWhich developer: ')
            
            dev_lst = by_dev_with_disc(master_dictionary, discount_dict, dev)
            
            # Check if list of games is empty
            if len(dev_lst) != 0:
                print("\nGames made by {} which offer discount:".format(dev))
                
                # Display games separated by a comma and space
                print(', '.join(dev_lst))
            else:
                print("\nNothing to print")
            
            option = input(MENU)
            
            option = int(option)
            
            # Check if option input is within 1-7
            while option not in range(1,8):
                print("\nInvalid option")
                option = input(MENU)
                option = int(option)
            
    # Display closing message
    print("\nThank you.")
    


if __name__ == "__main__":
    main()
      