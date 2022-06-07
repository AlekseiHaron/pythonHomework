from datetime import datetime
from file_to_file import FileToFile
from csv_parsing import CSVParsing

class Publish:
    def __init__(self, base_text):
        self.text = base_text


class News(Publish):

    def __init__(self, base_text, city):
        Publish.__init__(self, base_text=base_text)
        self.city = city

    def pub_time(self):
        now_date = datetime.now()
        date_time = now_date.strftime("%m/%d/%Y, %H:%M")
        return date_time

    def write_news_to_file(self):
        f = open(r"Test.txt", "a")
        f.write(f'\nNews:\n{self.text}\n{self.city}: {self.pub_time()}\n')
        f.close()


class Adv(Publish):

    def __init__(self, base_text, input_future):
        Publish.__init__(self, base_text=base_text)
        self.input_date = input_future

    def pub_days(self):
        now = datetime.now()
        my_date = datetime.strptime(self.input_date, "%Y-%m-%d")
        future_date = my_date.date()
        current_date = now.date()
        days_left = future_date - current_date
        return days_left.days

    def write_adv_to_file(self):
        f = open(r"Test.txt", "a")
        f.write(f'\nPrivate Ad:\n{self.text}\nActual until: {self.input_date}, {self.pub_days()} days left\n')
        f.close()


class Jokes(Publish):

    def __init__(self, base_text, ending="READ MORE NEXT TIME"):
        Publish.__init__(self, base_text=base_text)
        self.ending = ending

    def write_joke_to_file(self):
        f = open(r"Test.txt", "a")
        f.write(f'\nJoke of the day:\n{self.text}\n{self.ending}\n')
        f.close()


#tool to which will do user generated news feed:
def main():
    while True:
        try:
            input_one = int(input('Enter 1 if you want to add feeds Manually,'
                                  '\nEnter 2 if you want to add feeds from File: '
                                  '\nEnter 3 to parsing from File to CSV: '))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if input_one not in [1, 2, 3]:
            print("Please enter correct number")
            continue
        else:
            print(input_one)
            break

    if input_one == 1:

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
            print("News:")
            a = News(input_news, input_city)
            a.pub_time()
            a.write_news_to_file()
            print(f'{a.text}\n{a.city}: {a.pub_time()}')

        if val == 2:
            input_adv = str(input(
                'Type your Advertisement text here: '))
            due_date = str(input("Type due date af Ad here(yyyy-mm-dd): "))
            print("Private Ad:")
            a = Adv(input_adv, due_date)
            a.pub_days()
            a.write_adv_to_file()
            print(f'{a.text}\nActual until: {a.input_date}, {a.pub_days()} days left')

        if val == 3:
            input_jokes = str(input(
                'Type your Jokes text here: '))
            print("Joke of the day:")
            a = Jokes(input_jokes)
            a.write_joke_to_file()
            print(f'{a.text}\n{a.ending}')

    if input_one == 2:
        print("File updated successfully with:\n")
        copy_from_file = FileToFile()
        copy_from_file.copy_from_file()

    if input_one == 3:
        print("File parsed successfully with:\n")
        file_to_csv = CSVParsing()
        file_to_csv.file_to_csv_first()
        file_to_csv.file_to_csv_second()


if __name__ == '__main__':
    main()
