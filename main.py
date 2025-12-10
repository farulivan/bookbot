def count_words(book_text):
  return len(book_text.split())

def get_book_text(book_path):
  with open(book_path) as f:
    return f.read()

def main():
  book_text = get_book_text("books/frankenstein.txt")
  num_words = count_words(book_text)
  print(f'Found {num_words} total words')

main()