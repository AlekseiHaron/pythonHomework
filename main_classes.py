from datetime import datetime
import json

class Publish:
    def __init__(self, base_text):
        self.text = base_text


class News(Publish):

    def __init__(self, news_text, city):
        Publish.__init__(self, base_text=news_text)
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

    def __init__(self, adv_text, input_future):
        Publish.__init__(self, base_text=adv_text)
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

    def __init__(self, joke_text, ending="READ MORE NEXT TIME"):
        Publish.__init__(self, base_text=joke_text)
        self.ending = ending

    def write_joke_to_file(self):
        f = open(r"Test.txt", "a")
        f.write(f'\nJoke of the day:\n{self.text}\n{self.ending}\n')
        f.close()

class ParsJson:
    def read_from_json(self):
        with open(r"Test.txt", "a") as input_text:
            conv_to_dict = json.load(open('json_file.json'))
            for i in range(len(conv_to_dict)):
                try:
                    if conv_to_dict[i]["type"].lower() == "news":
                        # type = conv_to_dict['type']
                        text = conv_to_dict[i]['text']
                        city = conv_to_dict[i]['location']
                        n = News(news_text=text, city=city)
                        n.write_news_to_file()
                        # print(n)
                    elif conv_to_dict[i]['type'].lower() == 'joke':
                        joke_text = conv_to_dict[i]['joke_text']
                        ending = conv_to_dict[i]['ending']
                        jk = Jokes(joke_text=joke_text, ending=ending)
                        jk.write_joke_to_file()

                    elif conv_to_dict[i]['type'].lower() == 'adv':
                        adv_text = conv_to_dict[i]['adv_text']
                        adv_date = conv_to_dict[i]['adv_date']
                        ad = Adv(adv_text=adv_text, input_future=adv_date)
                        ad.write_adv_to_file()
                except ValueError as e:
                    print(e)
                print(conv_to_dict[i])
