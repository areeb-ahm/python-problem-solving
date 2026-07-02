# Write function word_frequency(text). Takes sentence string. Returns dict mapping each word (lowercase) to count of occurrences. Ignore punctuation . , ! ?.

def word_frequency(text):
    text_list = text.split()
    for index, item in enumerate(text_list):
        text_list[index] = "".join(char for char in text_list[index] if char.isalpha()).lower()
    # print(text_list)

    dict = {}
    for item in text_list:
        if dict.get(item) == None:
            dict[item] = 1
        else:
            dict[item] += 1

    return dict

print(word_frequency("The cat sat. The cat ran!"))
print(word_frequency("The cat sat. the CAT ran!"))