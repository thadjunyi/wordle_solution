from word_list import word_list

answer = "PICKY"

try_list = ["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY"]
remaining_char = "Z"


def checkResult(string, answer):
    result = []
    string_list = list(string)

    for index in range(len(string_list)):
        char = string_list[index]
        if char == answer[index]:
            result.append('correct')
        elif char in answer:
            result.append('present')
        else:
            result.append('absence')
    return result

def extractChar(try_list, result_list):
    dict = {0: '', 1: '', 2: '', 3: '', 4: ''}
    char_list = []

    for list_index in range(len(result_list)):
        result = result_list[list_index]

        for item_index in range(len(list(result))):
            state = result[item_index]

            if state == 'correct':
                char = try_list[list_index][item_index]
                dict[item_index] = char
                char_list.append(char)
                
            elif state == 'present':
                char = try_list[list_index][item_index]
                char_list.append(char)

    return dict, char_list

result_list = [checkResult(item, answer) for item in try_list]
pos_dict, char_list = extractChar(try_list, result_list)

print(pos_dict)
print(char_list)

candidate = []

for word in word_list:
    append = True
    for key, value in pos_dict.items():
        if value != '' and word[key].upper() != value.upper():
            append = False
            break

    if append:
        candidate.append(word)

print(candidate)
    
