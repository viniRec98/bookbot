from stats import get_num_words, get_count_characters, get_sorted_count_characters, sort_value
import sys


#It takes a filepath as input and returns the contents of the file as a string
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents





#It prints to the console the actual number of words in the book
def main():

    #CLI logic in case there are not 2 arguments when executing the program
    #python3 main.py books/frankenstein.txt
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)





    
    my_dict = get_count_characters(get_book_text(sys.argv[1]))
    my_sorted_list = get_sorted_count_characters(my_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words ")
    print("--------- Character Count -------")
    
    for dict in my_sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()