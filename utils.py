import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return ''
