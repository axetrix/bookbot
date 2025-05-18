def get_num_words(content):
    words = content.split()

    return len(words)

def get_characters_count(content) -> dict[str, int]:
    c_dict = {}

    for character in content:
        char_lower = character.lower()

        c_dict[char_lower] = c_dict.setdefault(char_lower, 0) + 1;

    return c_dict

def sort_on(item: dict[str, int|str]) -> int:
    return item.get("num", -1)

def get_sorted_char_list(c_dict: dict[str, int]) -> dict[str, int]:
    list = []

    for char_lower, num in c_dict.items():
        if char_lower.isalpha():
            list.append({"char": char_lower, "num": num})

    list.sort(key=sort_on, reverse=True)

    return list

def print_counts_dict(list: list[dict[str, int|str]]):
    for item in list:
        print(f"{item.get("char")}: {item.get("num")}")
