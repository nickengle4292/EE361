def textToString(s):
    words = []
    current_word = ''
    for c in s:
        if c.isalpha() or c.isdigit() or c == '_':
            current_word += c
        else:
            if current_word:
                words.append(current_word)
                current_word = ''
    if current_word:
        words.append(current_word)
    return words
