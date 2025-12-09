def count_words(text):
    words_list = text.split()
    return len(words_list)

def count_characters(text):
    character_count = {}
    for character in text:
        if character.lower() in character_count:
            character_count[character.lower()] += 1
        else:
            character_count[character.lower()] = 1
    return character_count

def sort_characters(character_count_dict):
    sorted_items_by_count = sorted(character_count_dict.items(), key=lambda item: item[1], reverse = True)
    return sorted_items_by_count