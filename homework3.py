import re

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87. """

# check the number of whitespaces are 87:
count = 0

try:
    for i in text:
        if i.isspace():
            count = count + 1
    if count == 87:
        print("Success the number of whitespaces is: ", count)
    else:
        print("The number of whitespaces is not 87", count)
except Exception as e:
    print(f"Exception: {e}")

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
