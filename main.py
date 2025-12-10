from stats import count_words, get_book_text, count_characters

def main():
  book_text = get_book_text("books/frankenstein.txt")
  num_words = count_words(book_text)
  print(f'Found {num_words} total words')
  print(count_characters(book_text))

main()