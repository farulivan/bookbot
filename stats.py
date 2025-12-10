def count_words(book_text):
  return len(book_text.split())

def get_book_text(book_path):
  with open(book_path) as f:
    return f.read()