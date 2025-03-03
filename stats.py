def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters(char_count):
    sorted_chars = sorted(
        [{'char': char, 'count': count} for char, count in char_count.items() if char.isalpha()],
        key=lambda x: x['count'],
        reverse=True
    )
    return sorted_chars