import sys
import os

from stats import get_num_words, get_characters_count, get_sorted_char_list, print_counts_dict

def get_book_text(filepath: str) -> str:
    file_contents = ""

    with open(filepath, "r", encoding="UTF-8") as f:
        for line in f:
            file_contents += line

    return file_contents

def main(file_path):
    content = get_book_text(file_path)
    num_words = get_num_words(content)
    character_dict = get_characters_count(content);

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_counts_dict(get_sorted_char_list(character_dict))
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

if os.path.exists(sys.argv[1]):
    main(sys.argv[1])
else:
    print("Please send a file as an argument")
    sys.exit(1)