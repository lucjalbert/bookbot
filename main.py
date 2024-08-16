import sys

def main():
    book_path = input("Enter the path to a book to analyse: ")
    book = get_book_text(book_path)
    word_count = count_words(book)
    character_amount = count_characters(book)
    sorted_characters = dict_to_list(character_amount)

    print(f"--- Analysis of book: {book_path} ---")
    print(f" Your book contains: {word_count} words.")

    for key, count in sorted_characters:
        print(f"The letter '{key}' was found {count} times")
    
    print(f"--- Analysis successful ---")


def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        print("File path incorrect or missing")
        sys.exit()


def count_words(book):
    words = book.split()
    return len(words)


def count_characters(book):
    book_lowered = book.lower()
    dict_char = {}
    for c in book_lowered:
        if c.isalpha():
            dict_char[c] = dict_char.get(c, 0) + 1
    return dict_char


def dict_to_list(dict_char):
    dict_sorted = sorted(dict_char.items(), key=lambda item: item[1], reverse=True)
    return dict_sorted


main()