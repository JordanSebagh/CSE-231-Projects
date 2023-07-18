##########################################################
# Computer Project #10
# Algorithm
# Initiate the card game by calling init_game function
# Display the rules and the menu of options
# Display the current stock, tableau, and foundation
# Prompt for user input
# While the game has not been won:
#   If the user has chosen to move card from tableau to foundation:
#       Validate that this choice is acceptable
#       If it is valid, move card to foundation and check if game was won
#       If not won, display stock, tableau, and foundation and get user input
#       If not valid display stock, tableau, and foundation and get input
#   If the user has chosen to move card within tableau:
#       Validate that this choice is acceptable
#       If it is valid, move card to tableau column and check if game was won
#       If not won, display stock, tableau, and foundation and get user input
#       If not valid display stock, tableau, and foundation and get input
#   If the user has chosen to deal to the tableau:
#       Deal cards to tableau by calling deal_to_tableau function
#       Display stock, tableau, and foundation
#       Get user input
#   If the user has chosen to restart the game:
#       Print message saying game is restarting
#       Initiate the card game by calling init_game function
#       Display the rules and the menu of options
#       Display the current stock, tableau, and foundation
#       Prompt for user input
#   If the user has chosen to display the menu of choices:
#       Print the menu of choices
#       Display the current stock, tableau, and foundation
#       Prompt for user input
#   If the option input is empty:
#       Re-prompt user for input
#   If the user has chosen to quit the game:
#       Exit loop
#       Display message
# Check if user won game:
#   If True, display message
###########################################################

import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''


def init_game():
    '''
    Create empty lists for foundation and tableau storage
    Create the deck by calling the Deck class
    Shuffle the deck
    Deal 4 cards to the tableau
    Returns: stock (Class Deck), tableau (list of lists), foundation (list)
    '''
    # Initiate foundation
    foundation = []

    # Initiate tableau
    tableau = []

    # Create deck of cards
    deck = cards.Deck()

    # Shuffle deck of cards
    deck.shuffle()

    # Deal 4 cards to tableau
    for i in range(4):
        lst = []
        lst.append(deck.deal())

        # Append the list with card to tableau list
        tableau.append(lst)

    return deck, tableau, foundation


def deal_to_tableau(tableau, stock):
    '''
    Check if there are less than 4 cards left in stock
    If True, deal rest of cards to tableau
    Otherwise, deal 4 cards to the tableau
    tableau: list of lists
    stock: Class Deck
    Returns: nothing
    '''

    # Check if there are less than 4 cards left in stock
    if len(stock) < 4:
        for lst in tableau:

            # Deal rest of cards in stock to tableau
            lst.append(stock.deal())
    else:

        for lst in tableau:

            # Deal 4 cards to tableau
            lst.append(stock.deal())


def validate_move_to_foundation(tableau, from_col):
    '''
    Check if the desired column to move from is empty
    If True, print error statement and return False
    Otherwise, obtain the card to move, its rank, and suit
    Check if the card to move is an ace and change rank to 15 if True
    Iterate through every column in tableau
    Obtain the last card in every column with its suit and rank
    Check if the current suit and the card to move suit are the same
    If True, check if rank ofm current card is greater than card to move rank
    If True, return True
    Otherwise, print error message and return False
    Return False and print error message if none of these cases are True
    tableau: list of lists
    from_col: column to move card from (int)
    returns: Boolean
    '''

    # Check if the desired column to move from is empty
    if tableau[from_col] == []:

        print("\nError, empty column: {}".format(from_col + 1))
        return False

    else:
        # Obtain the desired card to move
        card_to_move = tableau[from_col][-1]

        # Obtain desired card to move rank
        card_to_move_rank = card_to_move.rank()

        # Obtain desired card to move suit
        card_to_move_suit = card_to_move.suit()

        # Check if desired card to move is an Ace
        if card_to_move_rank == 1:

            # Change ranking to make Ace the highest rank
            card_to_move_rank = 15

        # Iterate through every column in tableau
        for lst in tableau:
            if lst != []:

                # Get the last card in every column
                card = lst[-1]

                # Get the rank of card
                rank = card.rank()

                # Get the suit of card
                suit = card.suit()

                # Check if card is Ace
                if rank == 1:

                    # Change ranking to be highest rank
                    rank = 15

                # Check if two cards being compared are same
                if rank == card_to_move_rank and suit == card_to_move_suit:
                    continue

                # Check if suit of both cards are the same
                elif suit == card_to_move_suit:

                    # Check if rank is greater than desired card rank
                    if rank > card_to_move_rank:
                        return True
                    else:

                        print("\nError, cannot move {}.".format(card_to_move))
                        return False

        print("\nError, cannot move {}.".format(card_to_move))
        return False


def move_to_foundation(tableau, foundation, from_col):
    '''
    Check if the move to foundation is valid
    If valid, obtain the desired card to move
    Add the desired card to foundation list
    Remove card from tableau
    If not valid, do nothing
    tableau: list of lists
    foundation: list
    from_col: column to move card from (int)
    Returns: nothing
    '''

    # Check if the move to foundation is valid
    valid = validate_move_to_foundation(tableau, from_col)

    if valid:

        # Obtain the desired card to move to foundation
        card = tableau[from_col][-1]

        # Add card to foundation list
        foundation.append(card)

        # Remove card from tableau
        tableau[from_col].remove(card)

    else:
        pass


def validate_move_within_tableau(tableau, from_col, to_col):
    '''
    Check if the desired column to move to is not empty
    If not empty, print message and return False
    Check if the desired column to move a card from is empty
    If empty, print error message and return False
    Otherwise, return True
    tableau: list of lists
    from_col: column to move card from (int)
    to_col: column to move card to (int)
    Returns: Boolean
    '''

    # Check if the desired column to move to is not empty
    if tableau[to_col] != []:

        # Print error message
        print("\nError, target column is not empty: {}".format(to_col + 1))
        return False

    # Check if the desired column to move a card from is empty
    elif tableau[from_col] == []:

        # Print error message
        print("\nError, no card in column: {}".format(from_col + 1))
        return False
    else:
        return True


def move_within_tableau(tableau, from_col, to_col):
    '''
    Check if the move within tableau is valid
    If valid, obtain the desired card to move
    Add the desired card to the desired column list
    Remove the card from its old location
    If not valid, do nothing
    tableau: list of lists
    from_col: column to move card from (int)
    to_col: column to move card to (int)
    Returns: nothing
    '''

    # Check if the move within tableau is valid
    valid = validate_move_within_tableau(tableau, from_col, to_col)

    if valid:

        # Obtain the desired card to move
        card = tableau[from_col][-1]

        # Add the desired card to the desired column list
        tableau[to_col].append(card)

        # Remove the card from its old location
        tableau[from_col].remove(card)

    else:
        pass


def check_for_win(tableau, stock):
    '''
    Check if the stock is not empty
    If it is not empty, return False
    Otherwise, iterate through every list in tableau
    Iterate through every card in every list
    Obtain the rank of the cards in each list
    Check if the rank of the card is an Ace
    If True, continue to next card
    Otherwise, return False
    If all cards are Aces, return True
    tableau: list of lists
    stock: Class Deck
    returns: Boolean
    '''

    # Check if the stock is not empty
    if not stock.is_empty():
        return False
    else:

        # Iterate through every list in tableau
        for card in tableau:

            # Iterate through every card in every list
            for val in card:

                # Obtain the rank of each card
                rank = val.rank()

                # Check if the rank is an Ace
                if int(rank) == 1:

                    continue
                else:

                    # Return False if card is not Ace
                    return False
    # Return True if all cards are Aces
    return True


def display(stock, tableau, foundation):
    '''Provided: Display the stock, tableau, and foundation.'''

    print("\n{:<8s}{:^13s}{:s}".format("stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)

    assert maxm > 0   # maxm == 0 should not happen in this game?

    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""), end='')
            else:
                print("{:<8s}".format(" XX"), end='')
        else:
            print("{:<8s}".format(""), end='')

        # prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print("{:4s}".format(str(col[i])), end='')

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')

        print()


def get_option():
    '''
    Prompt for user option input
    Convert input to uppercase characters
    If the option input is 'D', return ['D']
    If option input is 'R', return ['R']
    If option input is 'H', return ['H']
    If option input is 'Q', return ['Q']
    If option input contains letter 'F':
    Try converting second character input to an integer type
    Check if the number is 0 or greater than 4
    If True, print error message and return empty list
    Otherwise, return a list that contains 'F' and column index
    If int conversion fails, print error message and return empty list
    If option input contains letter 'T':
    Try converting second and third character input to an integer type
    Check if either numbers is 0 or greater than 4
    If True, print error message and return empty list
    Otherwise, return a list that contains 'T' and column indexes
    If input does not match any case, print message and return empty list
    Returns: list 
    '''

    # Prompt for user option input
    option = input("\nInput an option (DFTRHQ): ")
    option_new = option.upper()

    # If the option input is 'D', return ['D']
    if option_new == 'D':
        return ['D']

    # If option input is 'R', return ['R']
    elif option_new == 'R':
        return ['R']

    # If option input is 'H', return ['H']
    elif option_new == 'H':
        return ['H']

    # If option input is 'Q', return ['Q']
    elif option_new == 'Q':
        return ['Q']

    # Check if option input contains the letter 'F'
    elif 'F' in option_new:
        try:

            # Try converting second character to int type
            num1 = option[2]
            num1 = int(num1)

            # Check if the number is 0 or greater than 4
            if num1 == 0 or num1 > 4:

                # Print error message
                print("\nError in option: {}".format(option))
                return []

            num1 = int(num1) - 1

            # Return list of 'F' and column index
            return ['F', num1]

        except IndexError:
            print("\nError in option: {}".format(option))
            return []

    # Check if the letter 'T' is in user input
    elif 'T' in option_new:
        try:

            # Try converting values to int type
            num1 = option[2]
            num1 = int(num1)

            num2 = option[4]
            num2 = int(num2)

            # Check if either number is 0 or greater than 4
            if num1 == 0 or num2 == 0 or num1 > 4 or num2 > 4:

                print("\nError in option: {}".format(option))

                return []
            else:
                num1 = int(num1) - 1
                num2 = int(num2) - 1

                # Return a list of 'T' and two column indexes
                return ['T', num1, num2]
        except IndexError:
            print("\nError in option: {}".format(option))
            return []
    else:

        # Print error message if input does not match any case
        print("\nError in option: {}".format(option))
        return []


def main():
    '''
    Initiate the card game by calling init_game function
    Display the rules and the menu of options
    Display the current stock, tableau, and foundation
    Prompt for user input while the game has not been won:
    If the user has chosen to move card from tableau to foundation:
    Validate that this choice is acceptable
    If it is valid, move card to foundation and check if game was won
    If not won, display stock, tableau, and foundation and get user input
    If not valid display stock, tableau, and foundation and get input
    If the user has chosen to move card within tableau:
    Validate that this choice is acceptable
    If it is valid, move card to tableau column and check if game was won
    If not won, display stock, tableau, and foundation and get user input
    If not valid display stock, tableau, and foundation and get input
    If the user has chosen to deal to the tableau:
    Deal cards to tableau by calling deal_to_tableau function
    Display stock, tableau, and foundation
    Get user input
    If the user has chosen to restart the game:
    Print message saying game is restarting
    Initiate the card game by calling init_game function
    Display the rules and the menu of options
    Display the current stock, tableau, and foundation
    Prompt for user input
    If the user has chosen to display the menu of choices:
    Print the menu of choices
    Display the current stock, tableau, and foundation
    Prompt for user input
    If the option input is empty:
    Re-prompt user for input
    If the user has chosen to quit the game:
    Exit loop
    Display message
    Check if user won game:
    If True, display winning message
    '''

    # Initiate card game
    stock, tableau, foundation = init_game()

    print(RULES)
    print(MENU)

    # Display current stock, tableau, and foundation
    display(stock, tableau, foundation)

    # Get user input
    option = get_option()

    win = False

    # Iterate while the game has not been won
    while win == False:

        if 'F' in option:
            col = option[1]

            # Check if the move to foundation is valid
            valid = validate_move_to_foundation(tableau, col)
            if valid:

                # Move card to foundation if move is valid
                move_to_foundation(tableau, foundation, col)

                # Check if user hass won game
                win = check_for_win(tableau, stock)
                if win:
                    break

                # Display current stock, tableau, and foundation
                display(stock, tableau, foundation)

                # Get user input
                option = get_option()

            else:
                # Check if user has won game
                win = check_for_win(tableau, stock)
                if win:
                    break

                # Display current stock, tableau, and foundation
                display(stock, tableau, foundation)

                option = get_option()

        if 'T' in option:
            from_col = option[1]
            to_col = option[2]

            # Validate move within tableau
            valid = validate_move_within_tableau(tableau, from_col, to_col)
            if valid:

                # If valid, move card to desired column in tableau
                move_within_tableau(tableau, from_col, to_col)

                # Check if user has won game
                win = check_for_win(tableau, stock)
                if win:
                    break

                # Display current stock, tableau, and foundation
                display(stock, tableau, foundation)

                option = get_option()

            else:

                # Check if user has won game
                win = check_for_win(tableau, stock)
                if win:
                    break

                # Display current stock, tableau, and foundation
                display(stock, tableau, foundation)

                option = get_option()

        if 'D' in option:

            # Deal cards to tableau
            deal_to_tableau(tableau, stock)

            # Display current stock, tableau, and foundation
            display(stock, tableau, foundation)

            option = get_option()

        if 'R' in option:
            print("\n=========== Restarting: new game ============")

            # Initiate new game
            stock, tableau, foundation = init_game()
            print(RULES)
            print(MENU)

            # Display current stock, tableau, and foundation
            display(stock, tableau, foundation)
            option = get_option()

        if 'H' in option:
            print(MENU)

            # Display current stock, tableau, and foundation
            display(stock, tableau, foundation)
            option = get_option()

        if option == []:

            option = get_option()

        if option == ['Q']:

            print("\nYou have chosen to quit.")
            break

    if win:
        print("\nYou won!")


if __name__ == '__main__':
    main()


"\nInput an option (DFTRHQ): "
"\nError, empty column:"
"\nError, cannot move {}."
"\nError, no card in column:"
"\nError, target column is not empty:"
"\nError in option:"
"=========== Restarting: new game ============"
"\nYou have chosen to quit."
"\nYou won!"
