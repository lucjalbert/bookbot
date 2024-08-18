import os
import tkinter as tk
from tkinter import filedialog

def main():
    while True:
        content, name = get_book_text()
        word_count = count_words(content)
        character_amount, character_total = count_characters(content)
        sorted_characters = sort_dict(character_amount)

        # print a formatted report of the results
        print(f"--- Analysis of book: {name} ---")
        print(f"Your book contains: {word_count:,} words.")
        print(f"Your book contains: {character_total:,} letters.")

        for key, count in sorted_characters:
            print(f"The letter '{key}' was found {count:,} times")
        
        print(f"--- Analysis successful ---")

        # check if the user wants to continue before closing, this also serves as a way to keep
        # the program open and allow them to read the report
        go_again = restart()
        if go_again == False:
            break


# ask the user for their preferred method of input to provide their book
# return a string with the contents of the book and deduces the name of the book from the path
def get_book_text():
    while True:
        print("Launching Bookbot... please give me a book to analyse by:")
        print("1. Entering a file path (Type '1')")
        print("2. Browsing your files (Type '2')")

        # ask the user which method they prefer and stores the input
        choice = input("Your choice: ").strip().lower()

        if choice == "1":
            path = input("Please enter the file path: ").strip()
            content, name = read_file(path)
            if content:
                return content, name

        elif choice == "2":
            # call the filedialog window
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
            print("=================================")
            print("Invalid choice. Please try again.")
            print("=================================")


# attempt to read the file provided and handle errors
def read_file(path):
    try:
        with open(path, "rb") as f:
            try:
                content = f.read().decode("utf-8")
                return content, os.path.basename(path)
            except UnicodeDecodeError:
                print("===========================================================================")
                print("Incorrect file type, please only use text files such as: .txt, .md, or .csv")
                print("===========================================================================")
                return None, None
    except FileNotFoundError:
        print("==============================")
        print("File path incorrect or missing")
        print("==============================")
        return None, None



# take a string and turn it into a list of words before counting them and returning the amount
def count_words(book):
    words = book.split()
    return len(words)


# take a string and return a dictionary containing the amount of each character it contains
# upper and lower case are counted as the same character and punctuation is excluded
def count_characters(book):
    book_lowered = book.lower()
    characters = 0
    dict_char = {}
    for c in book_lowered:
        if c.isalpha():
            dict_char[c] = dict_char.get(c, 0) + 1
            characters += 1
    return dict_char, characters


# sort a dictionairy based on its values in descending order 
def sort_dict(dict_char):
    dict_sorted = sorted(dict_char.items(), key=lambda item: item[1], reverse=True)
    return dict_sorted


# ask the user if they would like to use the program again
def restart():
    while True:
        new_book = input("Would you like to analyze another book ? (Type Y or N): ").strip().lower()
        if new_book == "y":
            return True
        elif new_book == "n":
            return False
        else:
            print("=================================")
            print("Invalid choice. Please try again.")
            print("=================================")

main()