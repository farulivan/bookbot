import sys

from stats import count_words, get_book_text, count_characters, sort_characters, chars_dict_to_sorted_list

def main():
  # if len(sys.argv) != 2:
  #   print('Usage: python3 main.py <path_to_book>')
  #   sys.exit(1)
  book_path = './books/frankenstein.txt'
  book_text = get_book_text(book_path)
  num_words = count_words(book_text)
  characters_dict = count_characters(book_text)
  print(f'============ BOOKBOT ============')
  print(f'Analyzing book found at {book_path}...')
  print(f'----------- Word Count ----------')
  print(f'Found {num_words} total words')
  print(f'--------- Character Count -------')
  chars_sorted_list = chars_dict_to_sorted_list(characters_dict)
  print(chars_sorted_list)
  print('============= END ===============')

main()