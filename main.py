# main.py
import string

def Get_Book(path):

    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def Print_Book(book):
    print(book)

def Count_Words(book):
    words = book.split()
    return len(words)

def Count_Characters(book):
    alphabet_dict = {letter: 0 for letter in string.ascii_lowercase} 
    for char in book.lower():
        if char in alphabet_dict:
            alphabet_dict[char] += 1
    return alphabet_dict

def sort_on(dict):
    return dict["num"]

def main():
    """The main entry point of the program."""
    path = "books/frankenstein.txt"

    book = Get_Book(path)
    print(f"--- Begin report of {path}")
    print(f"{Count_Words(book)} words found")
    char_count = Count_Characters(book)

    # Convert to a list of dictionaries
    list_of_dicts = [{"name": k, "num": v} for k, v in char_count.items()]

    list_of_dicts.sort(reverse=True, key=sort_on)
    for dict in list_of_dicts:
        print(dict)
    print("End of report")

if __name__ == "__main__":
    main()
