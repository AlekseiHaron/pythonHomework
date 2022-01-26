import random

a_list = []
for i in range(100):
    a_list.append(random.randint(0, 1000))
"""
sort list from min to max (without using sort())
"""
for i in range(len(a_list)):
    for j in range(i + 1, len(a_list)):

        if a_list[i] > a_list[j]:
            a_list[i], a_list[j] = a_list[j], a_list[i]

print(a_list)


# here, the list we passed gets sorted and its last item is retrieved (item with index -1)
def my_max(my_list):
    return sorted(my_list)[-1]


# here, the list we passed gets sorted and its min item is retrieved (item with index 0)
def my_min(my_list):
    return sorted(my_list)[0]


print(my_max(a_list))
print(my_min(a_list))

"""
calculate average for even and odd numbers
"""
Even_Sum = 0
Odd_Sum = 0
Odd_cnt = 0
Even_cnt = 0
for num in a_list:
    if (num % 2 != 0):
        Odd_Sum = Odd_Sum + num
        Odd_cnt += 1
    else:
        Even_Sum = Even_Sum + num
        Even_cnt += 1

# average_Odd = Odd_Sum / len(a_list)
# average_Even = Even_Sum / len(a_list)

average_Odd = Odd_Sum / Odd_cnt
average_Even = Even_Sum / Even_cnt

print(Odd_Sum, Even_Sum)
print(Odd_cnt, Even_cnt)
print("Average of Odd list element is : ", average_Odd)
print("Average of Even list element is ", average_Even)