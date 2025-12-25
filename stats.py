#Returns the total number of words in a book
def get_num_words(book_as_string):
    list_of_words = book_as_string.split()
    return len(list_of_words)




#Returns the number of times each character appears in a book
def get_count_characters(book_as_string):
    
    count_characters_dict = {}

    for char in book_as_string:
        if char.lower() not in count_characters_dict:
            count_characters_dict[char.lower()] = 1
        else:
            count_characters_dict[char.lower()] += 1
            
    return count_characters_dict



#Takes the dictionary of characters and their counts and returns a sorted list of dictionaries
def sort_value(dict):
    """
    takes one dictionary from new_list
    
    returns the "num" value, (sorting key, value used to sort)
    """
    return dict["num"]


def get_sorted_count_characters(characters_counts_dict):

    new_list = []

    for key, value in characters_counts_dict.items():

        new_list.append({'char':key, 'num':value})
    
    new_list.sort(reverse=True, key=sort_value)
    
    return new_list


    


