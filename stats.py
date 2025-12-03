def get_word_count(book_string):
    split_string = book_string.split()
    return len(split_string)

def get_characters(letter_string):
    character_dict = {}
    lower_string = letter_string.lower()

    for character in lower_string:
        found =False
        for listing in character_dict:
            if character == listing:
                character_dict[listing] += 1
                found=True
                break
        if found !=True:
            character_dict[character] = 1
    return character_dict

def sort_characters(letter_dict):
    two_pairs= []
    for entry in letter_dict:
        two_pairs.append({"char": entry ,"num": letter_dict[entry]})
    
    two_pairs.sort(key=get_key,reverse=True)
    return two_pairs 

def get_key(list_item):

    key = list_item["num"]
    return key
    