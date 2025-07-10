def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(file):
    text = get_book_text(file) 
    cut_words = text.split()
    total_words = len(cut_words)
    return total_words 

def get_num_characters(file):
    char_dict = {}
    text = get_book_text(file)
    shorten = text.lower()
    for char in shorten:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_sort(dict):
    return dict["num"] 

def sorted_list(file):
    sorted = []
    char_dict = get_num_characters(file)
    for char,count in char_dict.items():
        if char.isalpha():
            sorted.append({"char": char, "num": count})
    sorted.sort(reverse=True, key=get_sort)
    return sorted
