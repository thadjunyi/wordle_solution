import time
from guess_list import string_list

#properties to tweak
#stores the max item in result list
result_count = 5
#stores the last index in the loop
last_index = 8258

#check for character duplication in a string
def duplicateCharInString(string):
    result_list = list(string)
    result_set = set(result_list)
    return len(result_list) != len(result_set)

#check for character duplication between 2 string
def duplicateCharBtwTwoString(string1, string2):
    result = string1 + string2
    return duplicateCharInString(result)

#stores the filtered string list
filtered_string_list = []

#if no character duplication in string, append to filtered string list
for string in string_list:
    if not duplicateCharInString(string):
        filtered_string_list.append(string)

print(f"Reduced original list length of {len(string_list)} to {len(filtered_string_list)}")
time.sleep(5)

#stores the final unique string combination
result = []
# last_index = -1
#stores the previous last index in the loop
prev_last_index = -1
#stores the indexes of the result list
indexes = []

while len(result) < result_count:

    #for each string in modified_string_list from the next item starting from the last index
    for index in range(last_index + 1, len(filtered_string_list)):
        string = filtered_string_list[index]

        #if result count matched, exit loop
        if len(result) >= result_count:
            break

        #if result count not matched
        else:
            append = True
        
            #for each item in result
            for item in result:

                #if there is character duplication between both string, set append flag to false
                if duplicateCharBtwTwoString(item, string):
                    append = False
                    break

            #if append flag is true, store the last index, append string into result, as well as the index of the string
            if append:
                last_index = index
                result.append(string)
                indexes.append(index)

    #if previous last index is same as last index, no more permutation of unique string can be found, set the last index to one level higher
    if prev_last_index == last_index:
        last_index = indexes[-1]
        print(f"Looped result: {result}")
        print(f"Indexes: {indexes}")

    #trim the result, indexes and store the last index to previous last index 
    result = result[:-1]
    indexes = indexes[:-1]
    prev_last_index = last_index

print(f"Final result: {result}")
