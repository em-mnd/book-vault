# This file manages the main menu and calls the right function when needed

def main_menu():
    main_choices = input('Welcome to the Book Vault. Please choose an option: 1. Books\n2. Exit') #I don't have ideas for options
    if not main_choices in ('1', '2'):
        raise ValueError('Please choose between option (1) or (2).')

# Trying to figure out if my classes should have their own menu since they (will) have multiple methods.