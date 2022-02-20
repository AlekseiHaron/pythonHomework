from datetime import datetime


class Publish:
    def __init__(self, base_text):
        self.x = base_text


#tool to which will do user generated news feed:
def main():
    while True:
        try:
            val = int(input(
                'Enter 1 if you want to add NEWS,\nEnter 2 if you want to add Private Ad,\nEnter 3 if you want to add Joke value,\nType here and click Enter: '))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if val not in [1, 2, 3]:
            print("Please enter correct number")
            continue
        else:
            print(val)
            break
    if val == 1:
        input_news = str(input(
            'Type here News and click Enter: '))
        input_city = str(input(
            'Type here City and click Enter: '))

        class News(Publish):
            print("News______")

            def __init__(self, base_text, city):
                Publish.__init__(self, base_text=base_text)
                self.y = city

            def pub_time(self):
                now_date = datetime.now()
                date_time = now_date.strftime("%m/%d/%Y, %H:%M")
                return date_time

        # now_date = datetime.now()
        # date_time = now_date.strftime("%m/%d/%Y, %H:%M")
        a = News(input_news, input_city)
        a.pub_time()
        print(f'{a.x}\n{a.y}: {a.pub_time()}')

        f = open(r"C:\Users\Oleksii_Kushnir\PycharmProjects\pythonHomework\Test.txt", "a")
        f.write(f'\n\nNews -------------------------\n{a.x}\n{a.y}: {a.pub_time()}')
        f.close()

    if val == 2:
        input_adv = str(input(
                   'Type your Advertisement text here: '))
        due_date = str(input("Type due date af Ad here(yyyy-mm-dd): "))
        my_date = datetime.strptime(due_date, "%Y-%m-%d")
        future_date = my_date.date()

        class Adv(Publish):
            print("Private Ad ------------------")

            def __init__(self, base_text, input_future):
                Publish.__init__(self, base_text=base_text)
                self.y = input_future

            def pub_days(self):
                now = datetime.now()
                current_date = now.date()
                days_left = future_date - current_date
                return days_left.days

        # now = datetime.now()
        # current_date = now.date()
        # days_left = future_date - current_date

        a = Adv(input_adv, future_date)
        a.pub_days()

        print(f'{a.x}\nActual until: {a.y}, {a.pub_days()} days left')

        f = open(r"C:\Users\Oleksii_Kushnir\PycharmProjects\pythonHomework\Test.txt", "a")
        f.write(f'\n\nPrivate Ad ------------------\n{a.x}\nActual until: {a.y}, {a.pub_days()} days left')
        f.close()

    if val == 3:
        input_jokes = str(input(
            'Type your Jokes text here: '))

        class Jokes(Publish):
            print("Joke of the day ------------")

            def __init__(self, base_text, ending="READ MORE NEXT TIME"):
                Publish.__init__(self, base_text=base_text)
                self.z = ending

        a = Jokes(input_jokes)
        print(f'{a.x}\n{a.z}')

        f = open(r"C:\Users\Oleksii_Kushnir\PycharmProjects\pythonHomework\Test.txt", "a")
        f.write(f'\n\nJoke of the day ------------\n{a.x}\n{a.z}')
        f.close()


if __name__ == '__main__':
    main()
