#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 20:57:27 2023

@author: jordansebagh
"""

###########################################################
# Computer Project #7
# Algorithm 
# Display opening message
# Prompt user to enter city names
# Prompt the user to enter an option
# If the user selects option 1:
#    Prompt user to enter start and end dates
#    Get data that falls under those dates
#    Prompt user for a desired category
#    Display error message if category is invalid and re-prompt for category
#    Display the maximum of that category for each city entered
# If the user selects option 2:
#    Prompt user to enter start and end dates
#    Get data that falls under those dates
#    Prompt user for a desired category
#    Display error message if category is invalid and re-prompt for category
#    Display the minimum of that category for each city entered
# If the user selects option 3:
#    Prompt user to enter start and end dates
#    Get data that falls under those dates
#    Prompt user for a desired category
#    Display error message if category is invalid and re-prompt for category
#    Display the average of that category for each city entered
# If the user selects option 4:
#    Prompt user to enter start and end dates
#    Get data that falls under those dates
#    Prompt user for a desired category
#    Display error message if category is invalid and re-prompt for category
#    Display the modes of that category for each city entered
# If the user selects option 5:
#    Prompt user to enter start and end dates
#    Get data that falls under those dates
#    Prompt user for a desired category
#    Display error message if category is invalid and re-prompt for category
#    Display the summary statistics of that category for each city entered
# If the user selects option 6:
#    Prompt user to enter start and end dates
#    Get data that falls under those dates
#    Prompt user for desired categories separarted by a comma
#    Display error message if a category is invalid
#    Display the cities with the highest and lowest average across all cities /
#    for each city
# If the user selects option 7:
#    Quit the program
# Display closing message
###########################################################


import csv
from datetime import datetime
from operator import itemgetter


COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    


MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''
        
      
        
def open_files():
    '''
    Prompt user to enter a series of cities separated by a comma
    Check if the filename is valid
    If valid, open the file and add the file pointer to a list
    If not, display error message 
    Returns: List of strings and list of file pointers
    '''
    
    
    fp_list = []

    city_names = input("Enter cities names: ")
    
    # Add cities to a list
    city = city_names.split(',')
    
    # Iterate through every city in the list
    for value in city:
        # Add the .csv extension to the city names
        name = value + '.csv'
        try:
            # Open file in read mode
            fp = open(name, 'r', encoding='utf-8')
            # Add file pointer to file pointer list
            fp_list.append(fp)
            
        except IOError:
            # Display error message
            print("\nError: File {} is not found".format(name))
            
            # Remove city from city list
            city.remove(value)
            
    return city, fp_list
    
    
    


def read_files(cities_fp):
    '''
    Reads all data from list of file pointers into a list of lists of tuples
    Iterate through every file pointer in file pointer list
    Skip first two header rows
    Iterate through the data in the files
    Convert values to float type
    Check if value is empty, and append None if True
    Otherwise, append the float value
    Create a tuple out of my list
    Append the running list to the master list
    cities_fp: list of file pointers
    Returns: List of lists of tuples
    '''
    
    
    big_list = []
    
    # Iterate through file pointers in the list
    for f_pointers in cities_fp:
        smaller_list = []
        
        # Read the csv files
        reader = csv.reader(f_pointers)
        
        # Skip header rows
        next(reader) 
        next(reader)
        
        # Iterate through every row in the file
        for data in reader:
            my_list = []
            
            # Iterate through every value in the row
            for values in data:
                try:
                    # Convert value to float type
                    values = float(values)
                except ValueError:
                    # Check if value is empty
                    if values == '':
                        # Append None to list
                        values = None
                # Append the row of data to a list
                my_list.append(values)
            
            # Append a tuple of the list to bigger list
            smaller_list.append(tuple(my_list))
        
        # Add the running list to a master list 
        big_list.append(smaller_list)
        f_pointers.close()
        
            
    return big_list
    
    
    
    
    

def get_data_in_range(master_list, start_str, end_str):
    '''
    Use the datetime operator to convert dates to comparable strings
    Iterate through every list inside the master list
    Iterate through every tuple within the lists
    Compare the date inside the tuple to the input date
    If the date is within the input date range, add the tuple to a list
    Add the running list to a master list
    master_list: list of lists of tuples
    start_str: start date string
    end_str: end date string
    Returns: List of lists of tuples
    '''

    big_list = []

    # Use datetime operator to convert dates to comparable strings
    start_date = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_str, "%m/%d/%Y").date()
    
    # Iterate through lists inside master_list
    for sub_list in master_list:
        my_list = []
        # Iterate through tuples inside lists
        for value in sub_list:
            # Extract the date inside the tuple
            compare_date = datetime.strptime(value[0], "%m/%d/%Y").date()
            # Compare the extracted date to the input dates
            if compare_date >= start_date and compare_date <= end_date:
                my_list.append(value)
        big_list.append(my_list)

    
    return big_list
            


    


def get_min(col, data, cities): 
    '''
    Iterate through every city in the city list
    Iterate through tuples inside specific list that corresponds to the city
    Skip the line if the value at specific index is None
    If the value at specific index is less than minimum, new min is created
    Append a tuple of the city and minimum to a running list
    col: index colum (int)
    data: list of lists of tuples
    cities: list of strings
    Returns: list of tuples
    '''

    i = 0
    minimum = 10000000
    my_list = []

    # Iterate through every city in the city list
    for city in cities:
        minimum = 10000000
        
        # Iterate through tuples inside specific list that corresponds to city
        for tup in data[i]:
            
            # Skip the line if the value at specific index is None
            if tup[col] == None:
                continue
            
            # Check if value at specific index is less than minimum
            elif tup[col] < minimum:
                
                # New min is created 
                minimum = tup[col]
            
        # Append a tuple of the city and maximum to a running list
        my_list.append(((city,minimum)))  

        i+=1  

    return my_list
            


    
    
    
    




        
def get_max(col, data, cities): 
    '''
    Iterate through every city in the city list
    Iterate through tuples inside specific list that corresponds to the city
    Skip the line if the value at specific index is None
    If the value at specific index is greater than maximum, new max is created
    Append a tuple of the city and maximum to a running list
    col: index colum (int)
    data: list of lists of tuples
    cities: list of strings
    Returns: list of tuples
    '''
    
    
    i = 0
    maximum = 0
    my_list = []

    # Iterate through every city in the city list
    for city in cities:

        
        maximum = 0
        
        # Iterate through tuples inside specific list that corresponds to city
        for tup in data[i]:

            # Skip the line if the value at specific index is None
            if tup[col] == None:
                continue

            # Check if value at specific index is greater than maximum
            elif tup[col] > maximum:
                # New max is created
                maximum = tup[col]
                
        # Append a tuple of the city and maximum to a running list
        my_list.append(((city,maximum)))  

        i+=1  

    return my_list
            
    
    
    
    


def get_average(col, data, cities): 
    '''
    Iterate through every city in the city list
    Iterate through tuples inside specific list that corresponds to the city
    Skip the line if the value at specific index is None
    Add the value at the specific index to a running average
    Add 1 to the count
    Calculate average by dividing the total by the count
    Append a tuple of the city and average to a running list
    col: index colum (int)
    data: list of lists of tuples
    cities: list of strings
    Returns: list of tuples
    '''
    
    
    
    i = 0
    count = 0
    average = 0
    my_list = []

    # Iterate through every city in the city list
    for city in cities:
        count = 0
        average = 0

        # Iterate through tuples inside specific list that corresponds to city
        for tup in data[i]:

            # Skip the line if the value at specific index is None
            if tup[col] == None:
                continue
            else:
                
                # Add value to running total
                average += tup[col]
                count += 1
        
        # Calculate average
        average = round(average / count, 2)

        # Append a tuple of the city and average to a running list
        my_list.append(((city,average)))  

        i+=1  

    return my_list


def tolerance(n1, n2):
    '''
    This function takes in two values and checks if the are within tolerance
    Try calculating absolute relative difference
    Except ZeroDivisionError
    Return True if the absolute relative difference is within tolerance
    Otherwise, return False
    n1: (float)
    n2: (float)
    Returns: boolean
    '''
    
    
    try:
        # Try calculating absolute relative difference
        value = abs((n1 - n2) / n1)
        x = 1
    # Except ZeroDivisionError
    except ZeroDivisionError:
        x = 0
    if x != 0:
        # Return True if absolute relative difference is within tolerance
        if abs(value) <= TOL:
            return True
        else:
            return False
    
    
    
    
    


def get_modes(col, data, cities):
    '''
    Iterate through every list inside and every city in parallel order
    Iterate through every tuple within the lists
    Skip the line if the value at specific index is None
    Otherwise, append the value at the specific index to a list
    Sort the list
    Iterate through every index within the range of the length of the list
    Pass numbers to the tolerance function to test for tolerance
    If the values are tolerant, make both values the same 
    Add 1 to the streak
    Otherwise, if the max streak is less than current streak, current streak
    is now the max streak
    Add the specifc value as a mode to a list
    If the max streak and current streak are equal, add the value to mode list
    Otherwise, continue checking values
    If the max streak is equal to zero in the end, modes list is empty
    Append a tuple of the city, modes list, and max_streak to the return list
    col: index column (int)
    data: list of lists of tuples
    cities: list of strings
    Returns: list of tuples
    '''
    
    
    final_list = []
    
    # Iterate through every list inside and every city in parallel order
    for lst, city in zip(data, cities):
        my_list = []
        
        # Iterate through every tuple within the lists
        for tup in lst:
            
            # Skip the line if the value at specific index is None
            if tup[col] == None:
                continue
            
            # Otherwise, append the value at the specific index to a list
            my_list.append(tup[col])
        
        # Sort the list
        my_list.sort()
        streak = 0
        max_streak = 0

        modes_list = []
        
        # Iterate through every index within the range of length of the list
        for index in range(len(my_list) - 1):
            
            # Pass numbers to the tolerance function to test for tolerance
            is_tolerant = tolerance(my_list[index], my_list[index + 1])
            
            # If the values are tolerant, make both values the same 
            if is_tolerant:
                my_list[index + 1] = my_list[index]
                
                # Add 1 to the streak
                streak += 1
                
            else:
                # Check if current streak is greater than max streak
                if streak > max_streak:
                    # Replace max streak with the current streak
                    max_streak = streak
                    # Add the specifc value as a mode to a list
                    modes_list = [my_list[index]]
                
                # Check if current and max streak are equal
                elif streak == max_streak:
                    # Add the value to mode list
                    modes_list.append(my_list[index])
                else:
                    pass
                streak = 0
        
        # Check if max streak is less than current streak
        if streak > max_streak:
            # Replace max streak with current streak
            max_streak = streak
            
            # Add the value to modes list
            modes_list = [my_list[index]]
        
        # Check if max streak and current streak are equal
        elif streak == max_streak:
            # Add value to modes list
            modes_list.append(my_list[index])
        else:
            pass
        
        # Create empty modes list if max streak is zero
        if max_streak == 0:
            
            modes_list = []
            
        # Create a tuple of the city, modes list, and max streak
        my_tuple = (((city, modes_list, max_streak + 1)))
        
        # Append tuple to list
        final_list.append(my_tuple)
    
    return final_list



    
    
    
def high_low_averages(data, cities, categories):
    '''
    Itrerate through every category in category list
    Check if category is valid
    If not valid, add None to list
    Otherwise, get the average of the category 
    Append the average to list
    Iterate through values in the average values list
    If the value is None, append None to return list
    Otherwise, sort the list by name then value
    Add sorted list to running list
    Iterate through tuples in the sorted lists
    Try extracting the minimum and maximum values of the tuple
    If TypeError is raised, append None to return list
    data: list of lists of tuples
    cities: list of strings
    categories: list of strings
    Returns: list of lists of tuples
    '''
    
    
    my_list = []
    
    return_list = []
    
    # Itrerate through every category in category list
    for category in categories:
        
        # Check if category is valid
        if category not in COLUMNS:
            # If not valid, add None to list
            my_list.append(None)
        else:
            
            col = COLUMNS.index(category)
            # Get the average of the category 
            avg = get_average(col, data, cities)
            my_list.append(avg)

    sorted_lists = []
    
    # Iterate through values in list
    for values in my_list:
        
        # Check if value is None
        if values == None:
            # Append None to list
            sorted_lists.append(None)
        else:
            # Sort list by name then value
            sorted_lst = sorted(values, key=itemgetter(0))
            sorted_lst = sorted(sorted_lst, key=itemgetter(1))
            sorted_lists.append(sorted_lst)
    
    # Iterate through tuples in list
    for tup in sorted_lists:
        x = []
        try:
            # Get the minimum
            minimum = tup[0]
            
            x.append(minimum)
            
            # Get the maximum
            maximum = tup[-1]
            
            x.append(maximum)
            
            return_list.append(x)
        except TypeError:
            # Append None to list if value is None
            return_list.append(None)
            
    return return_list


def display_statistics(col,data, cities):
    '''
    Get the minimum values by calling get_min function
    Get the maximum values by calling get_max function
    Get the average values by calling get_average function
    Get the mode values by calling get_modes function
    Iterate through values in range of the length of cities list
    Display the city, min, max, average, and modes of the city 
    col: index column (int)
    data: list of lists of tuples
    cities: list of strings
    Returns: nothing
    Displays: city, min, max, average, and modes
    '''
    
    # Get the minimum values by calling get_min function
    minimum = get_min(col, data, cities)
    
    # Get the maximum values by calling get_max function
    maximum = get_max(col, data, cities)
    
    # Get the average values by calling get_average function
    average = get_average(col, data, cities)
    
    # Get the mode values by calling get_modes function
    modes = get_modes(col, data, cities)
    
    # Iterate through values in range of the length of cities list
    for i in range(len(cities)):
        
        # Display city
        print("\t{}: ".format(cities[i]))
        
        # Display min, max, and average
        print("\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}".format(minimum[i][1], maximum[i][1], average[i][1]))
        
        # Display modes
        if modes[i][1] != []:
            print("\tMost common repeated values ({:d} occurrences): {:.1f}\n".format(modes[i][2], modes[i][1][0]))
        else:
            print("\t{}.".format('No Modes'))

        
def main():
    '''
    Display opening message
    Prompt user to enter city names
    Prompt the user to enter an option
    If the user selects option 1, prompt user to enter start and end dates
    Get data that falls under those dates
    Prompt user for a desired category
    Display error message if category is invalid and re-prompt for category
    Display the maximum of that category for each city entered
    If the user selects option 2, prompt user to enter start and end dates
    Get data that falls under those dates
    Prompt user for a desired category
    Display error message if category is invalid and re-prompt for category
    Display the minimum of that category for each city entered
    If the user selects option 3, prompt user to enter start and end dates
    Get data that falls under those dates
    Prompt user for a desired category
    Display error message if category is invalid and re-prompt for category
    Display the average of that category for each city entered
    If the user selects option 4, prompt user to enter start and end dates
    Get data that falls under those dates
    Prompt user for a desired category
    Display error message if category is invalid and re-prompt for category
    Display the modes of that category for each city entered
    If the user selects option 5, prompt user to enter start and end dates
    Get data that falls under those dates
    Prompt user for a desired category
    Display error message if category is invalid and re-prompt for category
    Display the summary statistics of that category for each city entered
    If the user selects option 6, prompt user to enter start and end dates
    Get data that falls under those dates
    Prompt user for desired categories separarted by a comma
    Display error message if a category is invalid
    Display the cities with the highest and lowest average across all cities /
    for each city
    If the user selects option 7, quit the program
    Display closing message
    '''
    
    
    
    print(BANNER)
    
    # Obtain city list and file pointer list
    city_list, fp_list = open_files()
    
    # Obtain list of lists of tuples
    data = read_files(fp_list)
    
    
    option = input(MENU)
    option = int(option)


    while option != 7:
        
        if option == 1:
            
            # Prompt for start and end date input
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            
            # Get the data within range of dates
            dates_data = get_data_in_range(data, start_date, end_date)

            category = input("\nEnter desired category: ")
            
            category = category.lower()
            
            # Repeatedly re-prompt until category is valid
            while category not in COLUMNS:
                print("\n\t{} category is not found.")
                
                category = input("\nEnter desired category: ")
                
                category = category.lower()
            
            # Get the index of the category
            index = COLUMNS.index(category)
            
            # Get max values 
            max_values = get_max(index, dates_data, city_list)
        
            print("\n\t{}: ".format(category))
            
            # Display max values
            for tup in max_values:
                for value in range(len(tup)):
                    city = tup[0]
                    maximum = tup[1]
                print("\tMax for {:s}: {:.2f}".format(city, maximum))
                    

            
            option = input(MENU)
            option = int(option)
            
        
        if option == 2:
            
            # Prompt for start and end date input
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            
            # Get the data within range of dates
            dates_data = get_data_in_range(data, start_date, end_date)
            
            category = input("\nEnter desired category: ")
            
            category = category.lower()
            
            # Repeatedly re-prompt until category is valid
            while category not in COLUMNS:
                print("\n\t{} category is not found.")
                
                category = input("\nEnter desired category: ")
                
                category = category.lower()
            
            # Get the index of the category
            index = COLUMNS.index(category)
            
            # Get min values
            min_values = get_min(index, dates_data, city_list)
        
            print("\n\t{}: ".format(category))
            
            # Display all minimum values
            for tup in min_values:
                for value in range(len(tup)):
                    city = tup[0]
                    minimum = tup[1]
                print("\tMin for {:s}: {:.2f}".format(city, minimum))
                    

            
            option = input(MENU)
            option = int(option)
            
        if option == 3:
            
            # Prompt for start and end date input
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            
            # Get the data within range of dates
            dates_data = get_data_in_range(data, start_date, end_date)
            
            category = input("\nEnter desired category: ")
            
            category = category.lower()
            
            # Repeatedly re-prompt until category is valid
            while category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                
                category = input("\nEnter desired category: ")
                
                category = category.lower()
            
            # Get the index of the category
            index = COLUMNS.index(category)
            
            # Get average values
            average_values = get_average(index, dates_data, city_list)
        
            print("\n\t{}: ".format(category))
            
            # Display all average values
            for tup in average_values:
                for value in range(len(tup)):
                    city = tup[0]
                    average = tup[1]
                print("\tAverage for {:s}: {:.2f}".format(city, average))
                    

            
            option = input(MENU)
            option = int(option)
        
        if option == 4:
            
            # Prompt for start and end date input
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            
            # Get the data within range of dates
            dates_data = get_data_in_range(data, start_date, end_date)
            
            category = input("\nEnter desired category: ")
            
            category = category.lower()
            
            # Repeatedly re-prompt until category is valid
            while category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                
                category = input("\nEnter desired category: ")
                
                category = category.lower()
            
            # Get the index of the category
            index = COLUMNS.index(category)
            
            print("\n\t{}: ".format(category))
            
            # Get mode values
            modes = get_modes(index, dates_data, city_list)
            
            # Display all mode values
            for tup in modes:

                print("\tMost common repeated values for {:s} ({:d} occurrences): {:.1f}\n".format(tup[0], tup[2], tup[1][0]))
                
            option = input(MENU)
            option = int(option)
    
        if option == 5:
            
            # Prompt for start and end date input
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            
            # Get the data within range of dates
            dates_data = get_data_in_range(data, start_date, end_date)
            
            category = input("\nEnter desired category: ")
            
            category = category.lower()
            
            # Repeatedly re-prompt until category is valid
            while category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                
                category = input("\nEnter desired category: ")
                
                category = category.lower()
            
            # Get the index of the category
            index = COLUMNS.index(category)
            
            print("\n\t{}: ".format(category))
            
            # Display summary statistics
            display_statistics(index, dates_data, city_list)
            
        
            option = input(MENU)
            option = int(option)

        if option == 6:
            
            # Prompt for start and end date input
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            
            # Get the data within range of dates
            dates_data = get_data_in_range(data, start_date, end_date)
            
            category = input("\nEnter desired categories seperated by comma: ")
            categories = category.split(',')
            
            print("\nHigh and low averages for each category across all data.")
            
            new_categories = []
            
            for category in categories:
                new_categories.append(category.lower())
            
            
            
            # Iterate through all categories
            for cat in new_categories:
                mini = 100000
                maxi = -100000
                cat = cat.lower()
                
                # Display error message if category is invalid
                if cat.lower() not in COLUMNS:
                    print("\n\t{} category is not found.".format(cat))
   
                    new_categories.remove(cat.lower())
                    continue
                else:
                    # Get index of category
                    index = COLUMNS.index(cat)
                    
                    # Get average values 
                    average_values = get_average(index, dates_data, city_list)
                    
                    # Iterate through average values and find high and lows
                    for tup in average_values:
                        if tup[1] < mini:
                            mini = tup[1]
                            mini_city = tup[0]
                        if tup[1] > maxi:
                            maxi = tup[1]
                            maxi_name = tup[0]
                    
                    # Display high and low averages for each category
                    print("\n\t{}: ".format(cat))
                    print("\tLowest Average: {:s} = {:.2f} Highest Average: {:s} = {:.2f}".format(mini_city, mini, maxi_name, maxi))

            option = input(MENU)
            option = int(option)
    
    # Display closing message
    print("\nThank you using this program!")
            
     


#DO NOT CHANGE THE FOLLOWING TWO LINES OR ADD TO THEM
#ALL USER INTERACTIONS SHOULD BE IMPLEMENTED IN THE MAIN FUNCTION
if __name__ == "__main__":
    main()
    
"Enter cities names: "
"\nError: File {} is not found"
#"\t{}: ".format(city)
#"\n\t{}: ".format(category)
"\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}"
"\tMost common repeated values ({:d} occurrences): {:s}\n"
"\tNo modes."
"\nEnter a starting date (in mm/dd/yyyy format): "
"\nEnter an ending date (in mm/dd/yyyy format): "
"\nEnter desired category: "
"\n\t{} category is not found."
"\tMax for {:s}: {:.2f}"
"\tMin for {:s}: {:.2f}"
"\n\t{}: "
"\tAverage for {:s}: {:.2f}"
"\tMost common repeated values for {:s} ({:d} occurrences): {:s}\n"
"\nEnter a starting date (in mm/dd/yyyy format): "
"\nEnter an ending date (in mm/dd/yyyy format): "
"\nEnter desired categories seperated by comma: "
"\nHigh and low averages for each category across all data."
"\tLowest Average: {:s} = {:.2f} Highest Average: {:s} = {:.2f}"
"\n\t{} category is not found."
"\nThank you using this program!"