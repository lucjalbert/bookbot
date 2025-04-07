# take a string and turn it into a list of words before counting them and returning the amount
def get_num_words(book):
    words = book.split()
    return len(words)