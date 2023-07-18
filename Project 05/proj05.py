#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:01:57 2023

@author: jordansebagh
"""
###########################################################
# Computer Project #5
# Algorithm 
# Display opening message and menu of options
# Prompt for menu option input
# Display error if user enters invalid option and prompt for input again
# If the user enters option 1:
#   Call the open file function to open file function
#   Call the read file function to get the data to output
#   Print the data to the user
#   Close the file
# If the user enters option 2:
#   Call the open file function to open file 
#   Prompt the user to enter an anime name to search for
#   Call the search anime function to get data
#   Print output to user
#   Close the file
# End the program if the user enters option 3
# Display closing message
###########################################################


def open_file():
    '''
    Repeatedly prompts for a filename until the file is opened successfully
    Use an exception handler to consider invalid filenames
    Return file pointer
    '''
    
    # Prompt for filename
    file_name = input("\nEnter filename: ")
    
    # Repeatedly prompt for filename until a valid one is entered
    while True:
        try:
            # Try to open file for reading
            fp = open(file_name, 'r', encoding='utf-8')
            
            # Return file pointer
            return fp
        # Exception handler to except invalid filename
        except IOError:
            print("\nFile not found!")
            file_name = input("\nEnter filename: ")
            
def find_max(num, name, max_num, max_name):
    '''
    Return the value and formatted name whose value is greater than max_num   
    Compare num parameter to max_num parameter:
        Return max_num and max_name if max_num is greater than num
    Compare num to max_num:
        return num and formatted name if num is greater than max_num
    Otherwise, return max_num and formatted name
    num: Initial number (float)
    name: Initial name (string)
    max_num: Current max number (float)
    max_name: Current min number (string)
    '''

    num = float(num)
    max_num = float(max_num)
    
    # Compare num to max_num
    if num < max_num:
        # Return max_num and name if condition is true
        return max_num, max_name
    # Compare num to max_num
    elif num > max_num:
        # Return num and formatted name if condition is true
        return num, "\n\t{}".format(name)
    else:
        # Return max_num and formatted name
        return max_num, "{}\n\t{}".format(max_name, name)
        

def find_min(num, name, min_num, min_name):
    '''
    Returns the value and name whose value is less than min_value
    Compare num parameter to min_num parameter:
        Return min_num and min_name if num is greater than min_num
    Compare num to min_num:
        return num and formatted name if min_num is greater than num
    Otherwise, return min_num and formatted name
    num: Initial number (float)
    name: Initial name (string)
    min_num: Current min number (float)
    min_name: Current min name (string)
    '''
    
    # Compare num to min_num
    if num > min_num:
        # Return min_num and min_name if condition is true
        return min_num, min_name
    # Compare num to min_num
    elif num < min_num:
        # Return num and formatted name if condition is true
        return num, "\n\t{}".format(name)
    else:
        # Return min_num and formatted name 
        return min_num, "{}\n\t{}".format(min_name, name)
    
def read_file(data_fp):
    '''
    Finds highest scoring title, highest ep. count title, lowest scoring title,
    and average score for all titles in the file
    Initiate starting values
    Iterate through the file:
        Assign title, score and episode variables with given indicies
        Check if score and episode are not 'N/A':
            If true, find the max and min score and title by calling the 
            find_max and find_min functions
            Find the max episode and max episode title by calling find_max
            Add 1 title number count 
        Check if score is not 'N/A':
            If true, find the max and min score and title by calling the 
            find_max and find_min functions
            Add 1 title number count
        Otherwise:
            Find max episode and max episode title only by calling find_max
    Compute average by dividing total score by total title numbers
    Return max_score, max_score_name, max_episodes, max_episode_name,
    min_score, min_score_name, and avg_score
    data_fp: file pointer object
    '''

    maximum = 0
    max_title = ''
    minimum = 100000
    min_title = ''
    total_score = 0
    title_num = 0
    max_episode = 0
    max_episode_title = ''
    
    # Iterate through the file
    for line in data_fp:
        title = line[0:100].strip()
        score = line[100:105].strip()
        episodes = line[105:110].strip()

        # Check if score and episode are not 'N/A'
        if score != 'N/A' and episodes != 'N/A':
            score = float(score)
            espisodes = float(episodes)
            
            # Find the max score and max score title
            maximum, max_title = find_max(score, title, maximum, max_title)
            # FInd the min score and min score title
            minimum, min_title = find_min(score, title , minimum, min_title)
            # Find the max episodes and max episodes title
            max_episode, max_episode_title = find_max(episodes, \
title, max_episode, max_episode_title)
            total_score += score
            title_num += 1
            
        # Check if only score is 'N/A'
        elif score != 'N/A':
            score = float(score)
            
            # Find the max score and max score title
            maximum, max_title = find_max(score, title, maximum, max_title)
        
            # FInd the min score and min score title
            minimum, min_title = find_min(score, title , minimum, min_title)
            
            total_score += score
            title_num += 1
        
        # Check if only episodes is 'N/A'
        elif episodes != 'N/A':
            
            # Find the max episodes and max episodes title
            max_episode, max_episode_title = find_max(episodes, title, \
max_episode, max_episode_title)

    # Compute average
    average = total_score / title_num
    
    anime_highest_score = maximum
    maxtitle = max_title
    highepcount = int(max_episode)
    maxeptitle = max_episode_title
    animelowscore = minimum
    mineptitle = min_title
    avgscore = round(average, 2)
    
    return anime_highest_score, maxtitle, highepcount, maxeptitle, \
animelowscore, mineptitle, avgscore

def search_anime(data_fp, anime_name):
    '''
    Reads through a file and returns the title and release season if it 
    contains the search string passed as parameter
    Iterate through each line in the file:
        Check if the anime name is in the file at specified index:
            Add 1 to count
            Add the title and release date to string
    If count is greater than 0:
        Add string to the output string
    Otherwise:
        Add message with no anime found to output string
    Return count of titles and the output containing title and release date
    data_fp: File pointer object
    anime_name: Anime name to search for (string)
    '''

    string = ''
    count = 0
    output = ''
    
    # Iterate through file
    for line in data_fp:
        
        # Check if anime name is in the file at specific indicies
        if anime_name in line[0:100]:
            
            count += 1
            # Add the title and release season to output string
            string += "\n\t{}{}".format(line[0:100], line[110:122])
    if count > 0:
        output += string
    else:
        # Add message to output string if no titles were found
        output += "\nNo anime with '{}' was found!".format(anime_name)
        
    
    return count, output
    
def main():
    '''
    Prompt the user for an option until the user decides to stop the program
    Display high score, max title, max episodes, lowest score, min episodes,
    and average score if user selects option 1
    Search the anime file if the user selects option 2 and print the count
    of titles with the matching input string
    Display closing message
    '''
    
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" 
    
    print(BANNER)
    print(MENU)
    
    choices = '1', '2', '3'
    
    option = input("\tEnter option: ")
    
    # Display error message if option is invalid
    while option not in choices:
        print("\nInvalid menu option!!! Please try again!")
        print(MENU)
        option = input("\tEnter option: ")
        
    # Loop until user selects option 3
    while option != '3':
        
        if option == '1':
            
            fp = open_file()
            # Get data by calling read file function
            high_score, max_title, max_ep, max_ep_title, low_score, \
min_ep, avg = read_file(fp)

            print("\n\nAnime with the highest score of \
{:.2f}:".format(float(high_score)))
            print("{}".format(max_title))
            print("\n\nAnime with the highest episode count \
of {:,}:".format(int(max_ep)))
            print("{}".format(max_ep_title))
            print("\n\nAnime with the lowest score of \
{:.2f}:".format(low_score))
            print("{}".format(min_ep))
            print("\n\nAverage score for animes in file is \
{:.2f}".format(avg))


            fp.close()
            
            
        elif option == '2':
            fp = open_file()
            anime_name = input("\nEnter anime name: ")
            
            # Get data by calling search anime function 
            count, output = search_anime(fp, anime_name)
            if count > 0:
                # Display message if there are more than 1 title that match
                print("\nThere are {} anime titles \
with '{}'".format(count, anime_name))
                print(output)
            else:
                # Display message if no titles were found with input
                print("\nNo anime with '{}' was found!".format(anime_name))


            fp.close()
            
        print(MENU)
        option = input("\tEnter option: ")
                 
    print("\nThank you using this program!")

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()