import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_column_index(header, col_letter):
    col_letter = col_letter.upper()
    index = ord(col_letter) - ord('A')
    if index < 0 or index >= len(header):
        return None
    return index
