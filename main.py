from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text
    
def print_report(path, text, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for character in sorted_list:
        print(f"{character[0]}: {character[1]}")
        


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_frankenstein = sys.argv[1]
        text = get_book_text(path_frankenstein)
        characters_book = count_characters(text)
        sorted_characters_count = sort_characters(characters_book)
        print_report(path_frankenstein, text, sorted_characters_count)



main()