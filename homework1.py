import random

a_list = []
for i in range(100):
    a_list.append(random.randint(0, 1000))

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


n = input(6)

n = int(n)

sum = 0

for num in range(0, n + 1, 1):

    if (not (num % 2) == 0):
        sum += num;

average = sum / n

print("SUM of odd numbers is: ", sum)
print("Average of odd numbers is: ", average)