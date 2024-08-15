def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f" Your book contains: {word_count} words.")


def get_book_text(path):   
    with open(path) as f:
        return f.read()


def count_words(book):
    book_words = book.split()
    return len(book_words)


main()