from random import randint, choice
from string import ascii_lowercase

final_dict, tmp_dict = {},  {}   # create tuples to use later for merge into one list and create one common dict with the biggest value
"""
create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter, 
dict's values should be a number (0-100), 
"""
rand_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]  #for dicts take lowercase letters in 1st for statement and take dict's values (0-100) in 2-nd sor statement
print(rand_list)

#Transform from list of dicts into dict of lists.
for dictionary in rand_list:                    #merge numbers in rand_list into one dict, example should be 'j': [90, 67] at the end
  for k, v in dictionary.items():               #items() return a new view of the dictionary’s items
    tmp_dict.setdefault(k, []).append(v)        #setdefault - If key is in the dictionary, return its value. If not, insert key with a value of default and return default. Adds a number (0-100) in list at the end of the dict
print(tmp_dict)

#Choose only the biggest one and create one common dict
for k, v in tmp_dict.items():                           # for item from previously dict to create a new view of the dicts items
  if len(v) > 1:                                        # if the number of items in a container (v)-number > 1
    final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)   # then take lowercase letters+"_"+index of the max number and max number
  else:
    final_dict[k] = v[0]                            # else take as is

# print(tmp_dict)
print(final_dict)