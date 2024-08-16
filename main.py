def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = count_words(book)
    character_count = count_characters(book)
    print(character_count)
    print(f" Your book contains: {word_count} words.")


def get_book_text(path):   
    with open(path) as f:
        return f.read()


def count_words(book):
    book_words = book.split()
    return len(book_words)


def count_characters(book):
    book_lowercase = book.lower()
    dict_char = {}
    alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    for letter in alphabet:
        amount = 0
        for character in book_lowercase:
            if character == letter:
                amount += 1
        dict_char[letter] = amount
    return dict_char


main()