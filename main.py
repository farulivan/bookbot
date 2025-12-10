from stats import count_words, get_book_text, count_characters, sort_characters

def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  num_words = count_words(book_text)
  characters_dict = count_characters(book_text)
  print(f'============ BOOKBOT ============')
  print(f'Analyzing book found at {book_path}...')
  print(f'----------- Word Count ----------')
  print(f'Found {num_words} total words')
  print(f'--------- Character Count -------')
  for char in sort_characters(characters_dict):
    print(f'{char['char']}: {char['count']}')
  print('============= END ===============')

main()