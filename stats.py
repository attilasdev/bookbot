def count_words(words):
    counter = 0
    new_words = words.split()
    for word in new_words:
        counter += 1
    return counter

def count_occurence(characters):
    new_dict = {}
    lowercase_characters = characters.lower()

    for char in lowercase_characters:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    
    return new_dict

def sort_chars_by_count(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=lambda item: item["count"])
    return chars_list