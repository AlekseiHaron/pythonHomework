import re
from random import randint, choice
from string import ascii_lowercase


print("==========================================Refactor_Homemork2:======================================================")

"""
create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter, 
dict's values should be a number (0-100), 
"""
def r_list():
    rand_list = []
    for j in range(randint(2, 10)):
        rand_list.append({choice(ascii_lowercase): randint(0, 100) for i in range(randint(0, len(ascii_lowercase)))})
    return rand_list


# method to create lists of random numbers of dicts
def create_list_of_rand_num_of_dicts(input):
    final_dict, tmp_dict = {}, {}

    for dictionary in input:
        for k, v in dictionary.items():
            tmp_dict.setdefault(k, []).append(v)
    for k, v in tmp_dict.items():
        if len(v) > 1:
            final_dict[k + "_" + str(v.index(max(v)) + 1)] = max(v)
        else:
            final_dict[k] = v[0]
    # print(final_dict)
    return final_dict



# give param to method
random_list = r_list()
print(random_list)
print(create_list_of_rand_num_of_dicts(random_list))

print("\n==========================================Refactor_Homemork3:======================================================")

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87. """


# method to check the number of whitespaces are 87:
def count_num_of_whitespaces(input_item):
    count = 0

    try:
        for i in input_item:
            if i.isspace():
                count = count + 1
        if count == 87:
            print("Success the number of whitespaces is:", count)
        else:
            print("The number of whitespaces is not 87", count)
    except Exception as e:
        print(f"Exception: {e}")
    return count

# give param to method
print(count_num_of_whitespaces(text))
print("======================================================")


# create method
def sentence_case(texts):
    # Lower text and replace
    # Split into sentences. Therefore, find all text that ends
    # with punctuation followed by white space or end of string.
    lower_text = texts.lower().replace("“iz”", " “iz”").replace(" iz ", " is ")
    sentences = re.findall('[^.!?\t]+[.:\n\n!?](?:\s)', lower_text)

    # Capitalize the first letter of each sentence
    sentences = [x[0].upper() + x[1:] for x in sentences]

    # Find last words of each sentence, create list with the result
    # Concat all
    last_words = re.findall(r'\w*\.', text)
    join_words = (' '.join(last_words).replace('.', '') + '.').capitalize()
    list_last_words = join_words.split(".")
    new_text = sentences[0:][:5] + ["\n\t"] + list_last_words[0:][:1] + [". "] + ["\n\n\t"] + sentences[5:]

    # Combine sentences
    return ''.join(new_text)


# use created method for homework text
print(sentence_case(text))

print("======================================================")




