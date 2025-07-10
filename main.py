import sys 
from stats import get_num_words, get_num_characters, sorted_list
 
def main():
    book = sys.argv[1]
    num_words = get_num_words(book)
    list_sorted = sorted_list(book)
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {book}...") 
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_sorted:
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============") 

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()

