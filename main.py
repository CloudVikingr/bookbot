# main.py

def main():
    """The main entry point of the program."""
    path = "books/frankenstein.txt"

    file_contents = ""

    with open(path) as f:
        file_contents = f.read()

    print(file_contents)

if __name__ == "__main__":
    main()
