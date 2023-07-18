#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:19:29 2023

@author: jordansebagh
"""

###########################################################
# Computer Project #4
# Algorithm 
# Print banner and the menu of options
# Prompt for user input of selection
# Loop while option not equal to 'x'
#   Repeatedly display error message if selection is not valid
#   Print the menu if the option input is 'm'
#   Display error message if option input is 'a' and input is invalid
#   Display decimal number conversion by calling to function if input is valid
#   Display error message if option input is 'b' and input is invalid
#   Display decimal number conversion by calling to function if input is valid
#   Display error message if option input is 'c' and input is invalid
#   Display decimal number conversion by calling to function if input is valid
#   If input is 'e' display error message if length of binary string is too big
#   Display error message if string is empty for input
#   Print the encoded binary string
#   If input is 'd' display the hiddent text inside the input binary string
#   Display closing message
###########################################################




MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''
    
def numtobase( N, B ):
    ''' 
    Converts a decimal number to binary in base B.
    N: Non-negative integer (string)
    B: Base (int)
    Create an empty string
    Error check if N value input is less than or equal to 0
        Return empty string if true
    Calculate quotient and remainder of input value N until quotient value is 0
    Return the reversed string with a total number of 8 digits
    '''
    
    string = ''
    N = int(N)
    
    if N <= 0:
        return string
    else:
        while True:
            
            # Calculate quotient
            calc = N // B
            
            # Calculate remainder
            remainder = N % B
            N = calc
            string += str(remainder)
            
            # End iteration when quotient is zero
            if N == 0:
                break
        # Reverse the string
        string = string[::-1]

        return string.zfill(8)


def basetonum( S, B ):
    '''
    Converts a binary string S in base B to an integer in base 10
    S: A number in base B (string)
    B: A base between 2 and 10 inclusive (int)
    Initialize total amount to add the products to after each iteration (total)
    Initialize the exponent at which the base will be raised to (length)
    Check if the user entered a string of digits or not
        Return 0 if true
    If false
        Iterate through each value in the string
        Raise the base to the power 
        Multiply the previous result by the digit that is being iterated
        Add the value to the running total each iteration
        Subtract 1 from count each iteration to reduce the exponent by 1
    Return an integer in base 10 representing the same number as 'S'
    '''
    
    
     
    total = 0
        
    length = len(S)
    
    count = length - 1
    
    
    if not(S.isdigit):
        return 0
    
    else:
        
        # Iterate through input string
        for i in S:
            i = int(i)
            
             # Raise input base to the power
            num = int(B)**count
             
            # Multiply result by value of 'i'
            num2 = i * num
        
            # Add value to running total
            total += num2
            
            count -= 1

    
        return total
        

def basetobase(B1, B2, s_in_B1):
    '''
    B1: A base (int)
    B2: A base (int)
    s_in _B1: A string representing a number in base B1
    Convert s_in_B1 to a number by passing it to the base_to_number function
    Convert previous result to the new base (B2) with the numtobase function
    Return 0 if s_in_B1 is 0
    If false, return a string representing the same number in B2
    '''
    
    
    string = ''
    
    # Convert input to number
    base_to_number = basetonum(s_in_B1, B1)
    
    # Convert result to new input base
    new_base_string = numtobase(base_to_number, B2)
    
    # If input is 0, return empty string
    if s_in_B1 == 0:
        return string
    else:
        x = new_base_string
        
    if len(x) > 8:
        return x.zfill(16)
    else:
        return new_base_string
    
    
    
def string_conversion(text, N):
    '''
    text: Input text to hide (string)
    N: Base (int)
    Iterate through each value in text input
        Add binary string representing the unicode character to empty string
        Convert this to the given base using the numtobase function
    Return the binary string representing the input text
    '''
    
    string = ''
    
    # Iterate through input text
    for i in text:
        
        # Convert to binary string
        count = ord(i)
        
        # Convert result to the input base
        string += numtobase(count, N)
    return string

 

def encode_image(image,text,N):
    '''
    image: Binary string (string)
    text: Text to hide in image (string)
    N: How many bits represent each pixel (int)
    Error check the given inputs
    Convert the input text to binary string using string_conversion function
    Iterate through the input image string
        Add the character to output string if the Nth character does not match
        Otherwise, add original digit to output string
        Break when the text has been iterated through completely
    Return output string with encoded text
    '''
    
    
    
    if image == '':
        return ''
    elif text == '':
        return image
    elif len(text) * N > len(image):
        return None
   
    output = ''
    j = 0
    text_done = False
    
    # Convert input text to binary
    text = string_conversion(text, 2)
    
    # Iterate through the input image string
    for i in range(len(image)):
        image_bit = image[i]
        
        # Add character to output string if Nth character does not match
        if (i+1) % N == 0 and text_done == False:
            output += text[j]
            j+=1
        else:
            # Add original digit to output string
            output += image_bit
       
        # Break when iteration is complete
        if j == len(text):
            text_done = True
    return output


def binary_to_text(binary_string, N):
    '''
    binary_string: Binary string that represents text (string)
    N: How many bits represent each pixel (int)
    Iterate through each 8th value in the binary string
        Convert 8 bit string to an integer and convert to ASCII character
        Add character to the string 
    Return string representing text message 
    '''
    
    string = ''
    
    x = len(binary_string)
    
    # Iterate through every 8 values in binary string input
    for i in range(0, x, 8):
        
        binary_character = binary_string[i:i+8]
        
        # Convert to ASCII character
        text_character = chr(int(binary_character, N))
        
        # Add character to string
        string += text_character
        
    return string
 

def decode_image(stego, N):
    '''
    stego: Binary string (string)
    N: How many bits represent each pixel (int)
    Iterate through stego input, with a step of N
        Add the value of i to the string for each iteration
    Truncate binary string to closest multiple of 8
        Truncate binary string to only consider multiple of 8 bits
    Pass the output to the text conversion function
    Return string representing the hidden text
    '''
    

    output = ''
    
    # Iterate through input every Nth value
    for i in range(N-1, len(stego), N):
        
        # Add value of 'i' to output string
        output += stego[i]
    
    # Truncate string to closest multiple of 8
    if int(len(output)) % 8 != 0:
        truncate = (int(len(output)) // 8) * 8
        
        output = output[:truncate]
    
    # Convert binary string to text
    output = binary_to_text(output, 2)
    
    return output
    


def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    print(MENU)
    choices = ('A', 'B', 'C', 'E', 'D', 'M', 'X')
    
    option = input("\n\tEnter option: ")
    option = option.upper()
    # Loop through until user enters 'x'
    while option != 'X':
        
        # Check if user entered a choice that is not valid
        while not(option in choices):
            print("\nError:  unrecognized option [{}]".format(option))
            print(MENU)
            option = input("\n\tEnter option: ")
            option = option.upper()
            
        if option == 'M':
            # Print the menu if user enters 'm'
            print(MENU)
            option = input("\n\tEnter option: ")
            option = option.upper()
            
        if option == 'A':
            
            decimal_number = input("\n\tEnter N: ")
            # Check if user entered a string with digits
            while not(decimal_number.isdigit()):
                print("\n\tError: {} was not a valid \
non-negative integer.".format(decimal_number))
                decimal_number = input("\n\tEnter N: ")
                
            base_number = int(input("\n\tEnter Base: "))
            # Error check if user entered valid input for base number
            while base_number < 2 or base_number > 10:
                print("\n\tError: {} was not a valid integer between 2 \
and 10 inclusive.".format(base_number))
                base_number = int(input("\n\tEnter Base: "))
            
            print("\n\t {} in base {}: \
{}".format(decimal_number,base_number,numtobase(decimal_number,base_number)))
                
            option = input("\n\tEnter option: ")
            option = option.upper()
            
        if option == 'B':
            
            basetonum_string = input("\n\tEnter string number S: ")
            basetonum_base = input("\n\tEnter Base: ")
            
            # Error check if user entered valid input for base
            while int(basetonum_base) < 2 or int(basetonum_base) > 10:
                print("\n\tError: {} was not a valid integer between 2 \
and 10 inclusive.".format(basetonum_base))
                basetonum_base = input("\n\tEnter Base: ")
                
            print("\n\t {} in base {}: {}".format(basetonum_string, \
basetonum_base, basetonum(basetonum_string, basetonum_base)))
            
            option = input("\n\tEnter option: ")
            option = option.upper()
        
        if option == 'C':
    
            string_number_base = int(input("\n\tEnter base B1: "))
            
            # Error check if user entered valid input for string number base
            while int(string_number_base) < 2 or int(string_number_base) > 10:
                print("\n\tError: {} was not a valid integer between 2 and \
10 inclusive.".format(string_number_base))
                string_number_base = int(input("\n\tEnter base B1: "))
                
            new_base = int(input("\n\tEnter base B2: "))
            
            # Error check if user entered valid input for base
            while int(new_base) < 2 or int(new_base) > 10:
                print("\n\tError: {} was not a valid integer between 2 and \
10 inclusive.".format(new_base))
                new_base = int(input("\n\tEnter base B2: "))
                 
            string_number = input("\n\tEnter string number: ")
            
            print("\n\t {} in base {} is {} in base {}...\
".format(string_number, string_number_base, \
basetobase(string_number_base, new_base, string_number), new_base))
            
            option = input("\n\tEnter option: ")
            option = option.upper()
            
        if option == 'E':
            
            binary_string = input("\n\tEnter a binary string of an image: ")
            num_pixels = int(input("\n\tEnter number of \
bits used for pixels: "))
            text_to_hide = str(input("\n\tEnter a text to \
hide in the image: "))
            
            x = string_conversion(text_to_hide, num_pixels)
            
            # Check to see if the image is too small to hold their text input
            if len(x) > len(binary_string):
                print("\n\tImage not big enough to hold \
all the text to steganography")
            
            
            # Check if user entered nothing for the string input
            elif binary_string == '':
                print("\n\tImage not big enough to hold all \
the text to steganography")
                
                
            else:
                
                # Print the encoded image if the input is valid
                print("\n\t Original image: {}".format(binary_string))
                print("\n\t Encoded image: \
{}".format(encode_image(binary_string,text_to_hide,num_pixels)))
            
            option = input("\n\tEnter option: ")
            option = option.upper()
            
        if option == 'D':
            
            encoded_string = input("\n\tEnter an encoded string of an image: ")
            num_bits = int(input("\n\tEnter number of bits used for pixels: "))
            # Print decoded message
            print("\n\t Original text: \
{}".format(decode_image(encoded_string, num_bits)))
            
            option = input("\n\tEnter option: ")
            option = option.upper()
            
            
            
    # Print closing message      
    print('\nMay the force be with you.')
        
        
    

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main()












"\n\tEnter option: "
"\n\tEnter N: "
"\n\tError: {} was not a valid non-negative integer."
"\n\tEnter Base: "
"\n\tError: {} was not a valid integer between 2 and 10 inclusive."
"\n\tEnter Base: "
"\n\t {} in base {}: {}"
"\nEnter string number S: "
"\n\tEnter base B1: "
"\n\tEnter base B2: "
"\n\t {} in base {} is {} in base {}..."
"\n\tEnter a binary string of an image: "
"\n\tEnter number of bits used for pixels: "
"\n\tEnter a text to hide in the image: "
"\n\t Original image: {}"
"\n\t Encoded image: {}"
"\n\tImage not big enough to hold all the text to steganography"
"\n\tEnter an encoded string of an image: "
"\n\tEnter number of bits used for pixels: "
"\n\t Original text: {}"
"\nError:  unrecognized option [{}]"
'\nMay the force be with you.'