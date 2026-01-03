#Counts the words in a text
def word_count(text):
    words = text.split()
    return f"Found {len(words)} total words"


#Counts characters in a text
def char_count(text):
    text_lower_case = text.lower()
    char_list = list(text_lower_case)
    str_to_int = {}
    for char in (char_list):
        if char in str_to_int:
            str_to_int[char] +=1
        else:
            str_to_int[char] = 1
    return str_to_int


#Takes a dictionary of characters and their counts and returns a sorted list of dictionaries. Special characters and spaces are discarded.
def char_sort(dictionary):
    items = []

    for char, count in dictionary.items():
        if char.isalpha():
            items.append({'char': char, 'num': count})
    items.sort(key=lambda x: x['num'], reverse=True)
    return items
