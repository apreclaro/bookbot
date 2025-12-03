import sys
from stats import get_word_count, get_characters, sort_characters


def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_string = get_book_text(sys.argv[1])
    num_words = get_word_count(book_string)
    print (
        f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    
    print (f"Found {num_words} total words")
    print (f"--------- Character Count -------")
    sorted_list = sort_characters(get_characters(book_string))
    for entry in sorted_list:
        if entry["char"].isalpha() == True:
            print(f"{entry["char"]}: {entry["num"]}")



def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()


