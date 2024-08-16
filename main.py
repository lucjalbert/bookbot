import sys

def main():
    book_path = input("Enter the path to a book to analyse: ")
    book = get_book_text(book_path)
    word_count = count_words(book)
    character_amount = count_characters(book)
    sorted_characters = sort_dict(character_amount)

    # prints a formatted report of the results
    print(f"--- Analysis of book: {book_path} ---")
    print(f" Your book contains: {word_count} words.")

    for key, count in sorted_characters:
        print(f"The letter '{key}' was found {count} times")
    
    print(f"--- Analysis successful ---")


# takes a path to a text file and returns a string with its content
# if the file path is incorrect or empty, prints error and terminates the program
def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        print("File path incorrect or missing")
        sys.exit()


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