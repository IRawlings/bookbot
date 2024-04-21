def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_book_words(text)
    letter_count = get_char_count(text)
    s = sort_on(letter_count)
    
    print(text)
    print(word_count)
    print(letter_count)
    print(s)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_words(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    # empty dict required
    letters = {}
    # convert book text to lower
    processed = book.lower()
    # look at every character of lowered text
    for char in processed:
        if char in letters:
                # Yes: add 1
            letters[char] += 1
        else:
                # No: add to dict with value of 1
                # letters[char] = 1 also works here, however [char] will not work with update, hence the f string
            letters.update({f"{char}": 1})
            # letters[char] = 1 # also works
    # return dict
    # don't forget to print returned result in main (following previous logic, but you could print it in the function)
    return letters
            
def sort_on(dict):
    return dict[0]

              
              
       


if __name__ == '__main__':
  main()


