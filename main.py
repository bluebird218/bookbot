def main():
    filepath = "books/frankenstein.txt"
    with open(filepath) as f:
        file_contents = f.read()
        lowercase_contents = file_contents.lower()
        words = lowercase_contents.split()
        num_words = len(words)
        book_dict = {}
        for word in words:
            word_dict = getLetters(word)
            book_dict = addDict(book_dict, word_dict)
    print(f"--- Begin report of {filepath} ---")
    print(f"{num_words} were found in the document")
    letter_list = makeList(book_dict)
    letter_list.sort(reverse=True, key=sort_on)
    for entry in letter_list:
        letter = entry["letter"]
        num = entry["num"]
        print(f"The {letter} character was found {num} times")
    print("--- End report ---")


def getLetters(word):
    letter_dict = {}
    for char in word:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

def addDict(dict1, dict2):
    add_dict = {}
    for i in dict1:
        if i in dict2:
            add_dict[i] = dict1[i] + dict2[i]
        else:
            add_dict[i] = dict1[i]
    for j in dict2:
        if j in dict1:
            add_dict[j] = dict1[j] + dict2[j]
        else:
            add_dict[j] = dict2[j]
    return add_dict

def makeList(dict):
    newList = []
    for entry in dict:
        if entry.isalpha():
            newList.append({"letter": entry, "num": dict[entry]})
    return newList

def sort_on(dict):
    return dict["num"]

main()