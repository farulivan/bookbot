def count_words(book_text):
  return len(book_text.split())

def get_book_text(book_path):
  with open(book_path) as f:
    return f.read()

def count_characters(book_text):
  characters = {}
  for char in book_text.lower():
    if char not in characters:
      characters[char] = 1
    else:
      characters[char] += 1
  return characters

def sort_on(char_count: tuple[str, int]):
    return char_count[1]

def sort_characters(characters_dict):
  character_list = []
  for char in characters_dict:
    if char.isalpha():
      character_list.append({"char": char, "count": characters_dict[char]})
  character_list.sort(reverse=True, key=sort_on)
  return character_list

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
  chars_list: list[tuple[str, int]] = []
  for char, count in chars_dict.items():
    chars_list.append((char, count))
  sorted_list = sorted(chars_list, key=sort_on, reverse=True)
  return sorted_list