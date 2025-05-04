from stats import get_num_words
from stats import count_characters
import sys

def main():
    #book_path="books/frankenstein.txt"
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path=sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    get_book_text(book_path)
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    print("----------- Word Count ----------")
    get_num_words(file_contents)

    print("--------- Character Count -------")
    counted_characters={}
    counted_characters= count_characters(file_contents)
    #print(counted_characters)
    
    # e: 44538
    for d_char in counted_characters:
        #print(f"{car.get('brand')}: {car.get('year')}")
        print(f"{d_char.get('char')}: {d_char.get('num')}")
        
    




main()