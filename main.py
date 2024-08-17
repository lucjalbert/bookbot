import os
import tkinter as tk
from tkinter import filedialog

def main():
    text, name = get_book_text()
    word_count = count_words(text)
    character_amount = count_characters(text)
    sorted_characters = sort_dict(character_amount)

    # prints a formatted report of the results
    print(f"--- Analysis of book: {name} ---")
    print(f" Your book contains: {word_count:,} words.")

    for key, count in sorted_characters:
        print(f"The letter '{key}' was found {count:,} times")
    
    print(f"--- Analysis successful ---")


# asks the user for their preferred method of input and saves the result as 
def get_book_text():
    while True:
        print("Launching Bookbot... please give me a book to analyse:")
        print("1. Enter a file path (Press '1')")
        print("2. Open the file explorer (Press '2')")

        choice = input("Your choice: ").strip().lower()

        if choice == '1':
            path = input("Please enter the file path: ").strip()
            content, name = read_file(path)
            if content:
                return content, name

        elif choice == '2':
            root = tk.Tk()
            root.withdraw()
            path = filedialog.askopenfilename()

            if path:
                content, name = read_file(path)
                if content:
                    return content, name
            else:
                print("No file was selected.")

        else:
            print("Invalid choice. Please try again.")

def read_file(path):
    try:
        with open(path, 'rb') as f:
            try:
                content = f.read().decode('utf-8')
                return content, os.path.basename(path)
            except UnicodeDecodeError:
                print("Incorrect file type, please use text files such as: .txt, .md, or .csv")
                return None, None
    except FileNotFoundError:
        print("File path incorrect or missing")
        return None, None



# takes a string and turns it into a list of words before counting them and returning the amount
def count_words(book):
    words = book.split()
    return len(words)


# takes a string and returns a dictionary containing the amount of each character it contains
# upper and lower case are counted as the same character and punctuation is excluded
def count_characters(book):
    book_lowered = book.lower()
    dict_char = {}
    for c in book_lowered:
        if c.isalpha():
            dict_char[c] = dict_char.get(c, 0) + 1
    return dict_char


# sorts a dictionairy based on the value of each key in descending order 
def sort_dict(dict_char):
    dict_sorted = sorted(dict_char.items(), key=lambda item: item[1], reverse=True)
    return dict_sorted


main()