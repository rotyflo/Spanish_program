import os

def clear_screen():
    """Clears screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    return