#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:00:56 2023

@author: jordansebagh
"""

import csv
from operator import itemgetter
import copy


###########################################################
# Computer Project #6
# Algorithm 
# Check condition to see if user entered option 4:
#   If option is not 4:
#       Check if option is 1
#       If option is 1:
#           Prompt user to input a book title
#           Call get books by criterion function to get all the books that
#           match the input title    
#           Print the book details of the returned list of tuples when calling
#           the criterion function
#           Prompt for option input
#       If option is 2: 
#           Prompt user for criteria input
#           Repeatedly prompt until the input has been successfully converted
#           to an integer type
#           If the user entered 6 for criteria, repeatedly prompt for a value
#           input until the value has successfully been converted to a float
#           If the user entered 7 for criteria, repeatedly prompt for a value
#           input until the value has successfully been converted to an int
#           Otherwise, prompt for a value input with no error checking
#           Get the books that match the value and criteria by calling
#           the get books by criterion function
#           Sort the books by calling the sort authors function
#           Display only the first 30 booksof the returned sorted books
#           Display the books and their information by calling display books
#           Prompt for user option input
#       If option is 3:
#           Prompt the user for a book category input
#           Repeatedly prompt for a rating input until the input has 
#           successfully been converted to a float
#           Repeatedly prompt for a page number input until the input has
#           succssfully been converted to an int
#           Prompt for a_z input to determine if the books being displayed
#           should be reversed
#           Prompt for keywords and add keywords to a list
#           Recommend a book by calling the recommend books function
#           Display the books and their information by calling display books
#           Prompt for user option input
# End program when option is 4
###########################################################



TITLE = 1
CATEGORY = 3
YEAR = 5
RATING = 6
PAGES = 7

MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "
                 
TITLE_FORMAT = '{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}'
TABLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}"

def open_file():
    '''
    Repeatedly prompts for a filename until the file is opened successfully
    Use an exception handler to consider invalid filenames
    Return file pointer
    '''
    
    file_name = input("Enter file name: ")
    
    # Repeatedly prompt for filename until a valid one is entered
    while True:
        try:
            # Try to open file for reading
            fp = open(file_name, 'r', encoding='utf-8')
            
            # Return file pointer
            return fp
        # Exception handler to except invalid filename
        except IOError:
            print("\nError opening file. Please try again.")
            file_name = input("Enter file name: ")
    


def read_file(fp):
    '''
    Reads the csv file using the file pointer.
    Skip the first header line
    Iterate through every value in the csv file.
    Assign each value in the file with a variable
    Add these variables for each book as a tuple to the master list
    fp: File Pointer
    Returns: list of tuples
    '''    
    
    # Read the csv file
    csv_reader = csv.reader(fp)
    next(csv_reader)
    
    i = 0
    my_list = []
    
    category_list = []
    
    # Iterate through every value in every line in the file
    for item in csv_reader:
        try:
            isbn13 = str(item[0])
            title = str(item[2])
            authors = str(item[4])
            categories = str(item[5])
            categories = categories.lower()
            category_list.append(categories)
            description = str(item[7])
            year = str(item[8])
            rating = float(item[9])
            num_pages = int(item[10])
            rating_count = int(item[11])
            
            # Add these values as a tuple to the master list
            my_list.append(((isbn13, title, authors, \
category_list[i].split(','), description, year, \
rating, num_pages, rating_count)))
            i += 1
        except ValueError:
            i += 1
            continue
        
    return my_list
            
    

def get_books_by_criterion(list_of_tuples, criterion, value):
    '''
    Retrieves all books that match a certain criterion
    Check if the criteria parameter is not valid, and if it is not valid,
    return an empty list
    If criterion is 1, iterate through the list of tuples and check
    which books match the value. If they match, add that book to the list
    If criterion is 3, iterate through the list of tuples and check
    which books match the value. If they match, add that book to the list
    If criterion is 5, iterate through the list of tuples and check
    which books match the value. If they match, add that book to the list
    If criterion is 6, iterate through the list of tuples and check
    which books are greater than or equal to the value. If true, 
    add that book to the list
    If criterion is 7, iterate through the list of tuples and check
    which books are within a range of 50 pages of the value. If true,
    add that book to the list
    list_of_tuples: List of tuples that contains all books
    criterion: Criteria to search for (int)
    value: Value to search for (int/float/string)
    Returns: List of tuples or one tuple
    '''    
    
    my_list = []
    
    criteria_options = (1, 3, 5, 6, 7)
    
    # Check if the criteria parameter is valid
    if criterion not in criteria_options:
        return my_list
    
    if criterion == 1:
        
        value = value.lower()
        # Iterate through master list of tuples
        for values in list_of_tuples:
            # Check if the value at certain index matches parameter value
            if values[1].lower() == value:
                # Add the tuple to the list if true
                my_list.append(values)
        # Check if the list is empty
        if len(my_list) > 0:
            for tup in my_list:
                return tup
        else:
            return my_list
        
    
    elif criterion == 3:

        value = value.lower()
        # Iterate through master list of tuples
        for line in list_of_tuples:
            
            for values in line[3]:
                # Check if the value at certain index matches parameter value
                if values == value:
                    # Add the tuple to the list if true
                    my_list.append(line)
        return my_list
        
    elif criterion == 5:
        
        value = str(value)
        # Iterate through master list of tuples
        for line in list_of_tuples:
            # Check if the value at certain index matches parameter value
            if line[5] == value:
                # Add the tuple to the list if true
                my_list.append(line)

        return my_list  
    
    elif criterion == 6:

        value = float(value)
        # Iterate through master list of tuples
        for line in list_of_tuples:
            # Check if the value at certain index matches parameter value
            if line[6] >= value:
                # Add the tuple to the list if true
                my_list.append(line)
        return my_list

                    
            
        
    elif criterion == 7:
        
        value = int(value)
        higher = value + 50
        lower = value - 50
        # Iterate through master list of tuples
        for line in list_of_tuples:
            # Check if value is in the range of 50 of the input value
            if line[7] == value or (line[7] >= lower and line[7] <= higher):
                # Add the tuple to the list if true
                my_list.append(line)
            
        return my_list
                                    
        
                

def get_books_by_criteria(list_of_tuples, category, rating, page_number):
    '''
    Filters books by category, rating, then page number
    Filter first by category by calling get_books_by_criterion function
    and passing the category parameter to the function
    Then, filter by rating by calling get_books_by_criterion function
    and passing the previous returned list of tuples and the 
    rating parameter to the function
    Then, filter by pages by calling get_books_by_criterion function and
    passing the previous returned list of tuples and the page number 
    parameter to the function
    list_of_tuples: List of tuples that contains all books
    category: category to filter by (string)
    rating: rating to filter by (float)
    page_number: number of pages to filter by (int)
    Returns: list of tuples
    '''
    
    # Call get_books_by_criterion function and pass category parameter
    category_tup = get_books_by_criterion(list_of_tuples, 3, category)

    # Call get_books_by_criterion and pass previous returned list of tuples
    rating_tup = get_books_by_criterion(category_tup, 6, rating)

    # Call get_books_by_criterion and pass previous returned list of tuples
    page_tup = get_books_by_criterion(rating_tup, 7, page_number)

    
    return page_tup
    
    
    

def get_books_by_keyword(list_of_tuples, keywords): 
    '''
    Retrieves all books whose description contains any of the keywords
    Convert all keywords to their lowercase version
    Iterate through the tuples
    Iterate through the words in the keyword list
    Check if the word in the keyword list matches any word in the tuple
    Add the book information to list if it is not already in it
    list_of_tuples: List of tuples that contains all books
    keywords: list of keywords to search for (list)
    Returns: list of tuples
    '''
    
    
    my_list = []

    new_keyword_list = []
    
    # Convert keywords to all lowercase
    for x in keywords:
        new_keyword_list.append(x.lower())
        
    # Iterate through the tuples
    for line in list_of_tuples:
        # Iterate through every word in the keyword list
        for word in new_keyword_list:
            # Check if any word in the description matches a word in the list
            if word.lower() in line[4].lower():
                # Add book info to list if it has not already been added
                if line not in my_list:
                    my_list.append(line)
                    


    return my_list
          


def sort_authors(list_of_tuples, a_z = True):
    '''
    Sort list of tuples by author name
    Make a copy of the list of tuples
    If the a_z parameter is True, sort the authors in ascending order
    Otherise, sort the authors in descending order
    list_of_tuples: List of tuples that contains all books
    a_z: Determines sorting order (Boolean)
    Returns: sorted list of tuples 
    '''
    
    
    # Make a copy of the master list of tuples
    new_list = copy.deepcopy(list_of_tuples)
    
    
    if a_z == True:
        # Sort the authors in ascending order 
        new_list = sorted(new_list, key=itemgetter(2))
    elif a_z == False:
        # Sort the authors in descending order
        new_list = sorted(new_list, key=itemgetter(2), reverse = True)
    
    
    
    return new_list
    

    
    
    
    
    
    






def recommend_books(list_of_tuples, keywords, category, rating, \
page_number,  a_z = True): 
    
    '''
    Recommends books based on input
    First, filter books by criteria by calling get books by criteria function
    and passing the parameters that were passed to this function
    Then, filter the books by keyword by calling get books by keyword function
    and passing the list of tuples returned by calling the previous function
    Then, sort the books by passing the list of tuples to the sort authors
    function
    list_of_tuples: List of tuples that contains all books
    keywords: list of keywords to search for (list)
    category: category to filter by (string)
    rating: rating to filter by (float)
    page_number: number of pages to filter by (int)
    a_z: Determines sorting order (Boolean)
    Returns: list of tuples
    '''
    # Filter by criteria by calling get books by criteria function
    by_criteria = get_books_by_criteria(list_of_tuples, category, \
rating, page_number)
    
    # Filter by keyword by calling get books by keyword function
    by_keyword = get_books_by_keyword(by_criteria, keywords)
   
    # Sort by the author name by calling sort authors function
    authors = sort_authors(by_keyword, a_z)
        
    return authors
    
    
    
    
    
    
    
    


def display_books(list_of_tuples):
    '''
    Display books with their informatiom
    Check if the list of tuples is empty, if True, display message
    Otherwise, display the book details by iterating through the list of tuples
    and checking if the author or title is less than 35 characters. If it is
    less than 35 characters, display the books details
    list_of_tuples: List of tuples that contains all books
    Returns: Nothing
    Displays: Book attributes
    '''

    # Check if the list of tuples is empty, if True, display message
    if len(list_of_tuples) < 1:
        print("\nBook Details:")
        print("Nothing to print.")
        
        
    else:
        print("\nBook Details:")
        print('{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}'.format(\
'ISBN-13', 'Title', 'Authors', 'Year', 'Rating', \
'Number Pages', 'Number Ratings'))
        
        # Iterate through list of tuples
        for line in list_of_tuples:
            # Check if the author or title is greater than 35 characters
            if len(line[1]) > 35 or len(line[2]) > 35:
                # Skip the line if True
                continue  

            # Display the book details
            print("{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}".format\
(line[0], line[1], line[2], line[5], line[6], line[7], line[8]))

                
        


def get_option():
    '''
    Displays a menu of options and prompts for input
    If option is not valid, display message and re-prompt for input
    Returns: Option (int)
    Displays: Menu and possible error message
    '''
    
    
    # Prompt for option input
    option = input(MENU)
    
    options = ('1', '2', '3', '4')
    
    # Check if option is valid
    while option not in options:
        # Display error message if invalid option
        print("\nInvalid option")
        
        option = input(MENU)
    return int(option)
    
    
    
def main():
    '''
    Call the open file function
    Call the read file function to get a list of tuples
    Call the get option function to get user input
    If option input is 1, prompt for a book title input
    Call the get books by criterion function to get a list of tuples 
    that represents the books that match bok title input
    Display the books details
    If the option is 2, repeatedly prompt for criteria input until it is
    converted to an integer
    If criteria input is 6, repeatedly prompt for value input until it is 
    converted to a float
    If criteria is 7, repeatedly prompt for a value input until it is
    converted to an int
    Otherwise, prompt for value input of any type
    Call get books by criterion
    Sort the books based on author name by calling sort authors function
    Display only the first 30 books
    Display the books by calling the display books function
    If the option is 3, prompt for category input
    Repeatedly prompt for rating input until converted to a float
    Repeatedly prompt for page number input until converted to an int
    Prompt for a_z input to determine the order of which to sort the books by
    Prompt for keywords and add the keywords to a list
    Call the recommend books function
    Display the recommended books by calling display books function
    If the option is 4, quit the program
    '''
    
    
    
    
    
    crit = (3, 5, 6, 7)
    
    fp = open_file()
    
    list_of_tuples = read_file(fp)
    
    option = get_option()
    
    
    while option != 4:
        
        if option == 1:
            
            # Prompt for book title
            book_title = input("\nInput a book title: ")
            
            # Search for matching books
            search = get_books_by_criterion(list_of_tuples, 1, book_title)
            print("\nBook Details:")
            print('{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}'.format\
('ISBN-13', 'Title', 'Authors', 'Year', 'Rating', \
'Number Pages', 'Number Ratings'))
            
            # Print book details
            print("{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}".format\
(search[0], search[1], search[2], search[5], search[6], \
search[7], search[8]))
            
            option = get_option()
            
            
        elif option == 2:
            # Repeatedly prompt until converted to an int
            while True:
                criteria = input(CRITERIA_INPUT)
                try:
                    criteria = int(criteria)
                    if criteria in crit:
                        break
                    else:
                        print("\nInvalid input")
                except ValueError:
                    print("\nInvalid input")
                    
            
            if criteria == 6:
                value = input("\nEnter value: ")
                # Repeatedly prompt until converted to a float
                while True:
                    try:
                        value = float(value)
                        break
                    except ValueError:
                        print("\nInvalid input")
                        value = input("\nEnter value: ")
                    
                    
            elif criteria == 7:
                value = input("\nEnter value: ")
                # Repeatedly prompt until cinverted to an int
                while True:
                    try:
                        value = int(value)
                        break
                    except ValueError:
                        print("\nInvalid input")
                        value = input("\nEnter value: ")
            else:
                value = input("\nEnter value: ")
                
            # Get the books that match the criteria and value input
            books = get_books_by_criterion(list_of_tuples, criteria, value)
            
            # Sort the books by author name
            sorted_books = sort_authors(books, 1)
            
            # Display only the first 30 books
            new = sorted_books[:30]
            
            # Display the books and their details
            displayed = display_books(new)
        
            option = get_option()
        
        
        elif option == 3:
            # Prompt for category input
            category = input("\nEnter the desired category: ")
            
            # Prompt for rating input and try to convert to a float
            rating = input("\nEnter the desired rating: ")
            
            try:
                rating = float(rating)
                
            except ValueError:
                print("\nInvalid input")
                rating = input("\nEnter the desired rating: ")
               
            # Prompt for page number input and try to convert to an int
            page_number = input("\nEnter the desired page number: ")
            try:
                page_number = int(page_number)
                
            except ValueError:
                print("\nInvalid input")
                page_number = input("\nEnter the desired page number: ")
                
                
            # Prompt for a_z input
            a_z = input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: ")
            a_z = int(a_z)
            
            if a_z == 1:
                a_z = True
            else:
                a_z = False
            
            
            keywords = input("\nEnter keywords (space separated): ")
            # Add keywords to a list 
            key_list = keywords.split(' ')
                
            # Recommend books based on user input
            recom = recommend_books(list_of_tuples, key_list, \
category, rating, page_number, a_z)
            
            # Display the recommended books
            display_books(recom)
            
            option = get_option()
            

# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()

"Enter file name: "
"\nError opening file. Please try again."
"\nInput a book title: "
"\nInvalid input"
"\nInvalid option"
"\nEnter value: "
"\nBook Details:"
"\nEnter the desired category: "
"\nEnter the desired rating: "
"\nEnter the desired page number: "
"\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: "
"\nEnter keywords (space separated): "
"Nothing to print."


