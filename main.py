import sys
import os

from stats import get_num_words, get_characters_count, get_sorted_char_list

def get_book_text(filepath: str) -> str:
    file_contents = ""

    with open(filepath, "r", encoding="UTF-8") as f:
        for line in f:
            file_contents += line

    return file_contents

def print_stats(file_path: str, num_words: int, sorted_list: list[dict]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        character = item.get("char")

        if character.isalpha():
            print(f"{character}: {item.get("num")}")
            
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print("Please send a file as an argument")
        sys.exit(1)

    file_path = sys.argv[1]
        
    content = get_book_text(file_path)

    num_words = get_num_words(content)
    character_dict = get_characters_count(content)
    sorted_list = get_sorted_char_list(character_dict)

    print_stats(file_path, num_words, sorted_list)


main()