def count_letters(list_of_words):
    letter_dict = {}
    for word in list_of_words:
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                if letter in letter_dict:
                    letter_dict[letter] += 1
                else:
                    letter_dict[letter] = 1
    return letter_dict

def print_report(letter_dict, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter, count in letter_dict.items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")
    return 

with open('./books/frankenstein.txt', 'r') as file:
    file_contents = file.read()
    words = file_contents.split()
    letter_dict = count_letters(words)
    sorted_letter_dict = dict(sorted(letter_dict.items(), key=lambda x: x[1], reverse=True))
    print_report(sorted_letter_dict, len(words))