import sys
from keywordFunctions import*

# pull filename from command line
filename = sys.argv[1]

# open an read the file that was passed in through command line
f = open(filename, "r")
text = f.read()

words = textToString(text)  # Convert the text to a string

contexts = {}
for i, word in enumerate(words):   # enumerate words so that we can loop through them
    if i >= 2 and i <= len(words) - 3:
        key = words[i].lower()
        context = ' '.join(words[i-2:i+3]) # add the two words before and after the keyword
        if key in contexts:
            contexts[key].append(context)
        else:
            contexts[key] = [context]
    elif i == 1:    # check for the second word
        key = words[i].lower()
        context = ' '.join(words[i-1:i+3])
        if key in contexts:
            contexts[key].append(context)
        else:
            contexts[key] = [context]
    elif i == 0:    # check for the first word
        key = words[i].lower()
        context = ' '.join(words[:i+3])
        if key in contexts:
            contexts[key].append(context)
        else:
            contexts[key] = [context]
    elif i == len(words)-2:     # check for the second to last word
        key = words[i].lower()
        context = ' '.join(words[i-2:i+2])
        if key in contexts:
            contexts[key].append(context)
        else:
            contexts[key] = [context]
    elif i == len(words) - 1:   # check for the last word
        key = words[i].lower()
        context = ' '.join(words[i-2:])
        if key in contexts:
            contexts[key].append(context)
        else:
            contexts[key] = [context]


while True:
    keyword = input('Enter a keyword or enter "Q" to quit: ').lower()
    if keyword == 'q':
        break
    if keyword in contexts:
        for context in contexts[keyword]:
            print(context)
    else:
        print('The keyword entered is not in the file.')
