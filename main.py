def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_book_words(text)
    letter_count = get_char_count(text)
    print(text)
    print(word_count)
    print(letter_count)
    char_report(letter_count, word_count)

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

        
def char_report(letter_data, wc):
    alphabet = [] 
    
    
    # Convert letter_data to a list of dicts for each entry. i.e {"name": "a", "num": 3454} from current format of {"a": 5345}
    # boot.dev does actually only care about isalpha() this time.
    for key in letter_data: 
        if key.isalpha():
            alphabet.append({"name": key, "num": letter_data[key]})
    
    # Call the sort function on the dict (inline)
    # call sort on the list, and sort largest first using the 'sort_on' function which will sort on the 'num' property
    alphabet.sort(reverse=True, key=sort_on)

    # Print the sorted varaible to the console in hte correct format with --- Start report --- and --- End Report --- 
    print("--- Start Report ---")
    print(f"{wc} words found in the document\n")
    for char in alphabet:
        print(f"The '{char['name']}' character was found {char['num']} times")
    print("--- End Report ---")

# Define a sort_on() function to sort on 'num' - largest first (reverse order)             
def sort_on(dict):
    return dict["num"]

       


if __name__ == '__main__':
  main()


