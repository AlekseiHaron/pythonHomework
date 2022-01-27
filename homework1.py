import random
"""
create list of 100 random numbers from 0 to 1000
"""
a_list = []   #create a list
for i in range(100):
    a_list.append(random.randint(0, 1000))  # for each item in range take range 100 , add random elements from 0-100 at the end
"""
sort list from min to max (without using sort())
"""
for i in range(len(a_list)):
    for j in range(i + 1, len(a_list)):

        if a_list[i] > a_list[j]:
            a_list[i], a_list[j] = a_list[j], a_list[i]

print(a_list)


# gets sorted the list, last item is retrieved (item with index -1) just for my understanding no need to check
def my_max(my_list):
    return sorted(my_list)[-1]

# gets the list sorted, min item is retrieved (item with index 0) just for my understanding no need to check
def my_min(my_list):
    return sorted(my_list)[0]

# print(my_max(a_list))
# print(my_min(a_list))

"""
calculate average for even and odd numbers
"""
Even_Sum = 0 #create var int for use in loop
Odd_Sum = 0
Odd_cnt = 0
Even_cnt = 0
for num in a_list:              # for each item in list next
    if (num % 2 != 0):          # check if number are Odd's or Even's
        Odd_Sum = Odd_Sum + num # Inside a loop, calculate the sum of odd numbers
        Odd_cnt += 1            # count of odd numbers
    else:
        Even_Sum = Even_Sum + num   # for Even's sum even numbers
        Even_cnt += 1               # count of even numbers


average_Odd = Odd_Sum / Odd_cnt         #formula sum odd / cnt odd
average_Even = Even_Sum / Even_cnt      #formula sum even / cnt even

# print(Odd_Sum, Even_Sum)
# print(Odd_cnt, Even_cnt)
print("Average of Odd list element is : ", average_Odd)
print("Average of Even list element is ", average_Even)