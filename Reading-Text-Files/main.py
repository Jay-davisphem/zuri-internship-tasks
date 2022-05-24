# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import re # for re.sub to remove punctuations, it's overkill though, So sorry.

def read_file_content(filename):
    # [assignment] returns file content
    with open(filename, 'r') as f:
        f = f.read()
    return f


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] count the number words of occurences in a file
    
    punct = r'[^\w\s]'
    text = re.sub(punct, '', text)

    container = {} # hash holding and instantiating count occurences
    for word in text.split():
        if word in container:
            container[word] += 1
        else:
            container[word] = 1
    return container

print(count_words())
