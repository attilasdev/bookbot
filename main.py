from stats import count_words, count_occurence, sort_chars_by_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 

def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {char_dict['count']}")
    
    print("============= END ===============")

def main():
    text = get_book_text(book_path)
    counted_words = count_words(text)
    character_number = count_occurence(text)
    print_report(book_path, counted_words, sort_chars_by_count(character_number))

main()