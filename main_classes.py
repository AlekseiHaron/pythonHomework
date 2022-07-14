from datetime import datetime
import json
import xml.etree.ElementTree as ET
import pyodbc
import sqlite3

class Publish:
    def __init__(self, base_text):
        self.text = base_text

a = Publish('tedfsdf')
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

class ParseJson:
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

class ParseXML:
    def read_from_xml(self):
        tree = ET.parse('xml_file.xml')
        root = tree.getroot()
        with open(r"Test.txt", "a") as f:
            for publish_article in root.findall('PublishArticle'):
                try:
                    if publish_article.get('name').lower() == 'news':
                        xml_text = publish_article.find('TypeData').find('Info').text
                        xml_city = publish_article.find('TypeData').find('Location').text
                        n = News(news_text=xml_text, city=xml_city)
                        n.write_news_to_file()
                        print(publish_article.attrib)
                        print(xml_text)
                        print(f'{xml_city}\n')
                    elif publish_article.get('name').lower() == 'advertising':
                        xml_adv_text = publish_article.find('TypeData').find('Adv_Info').text
                        xml_adv_date = publish_article.find('TypeData').find('Adv_Date').text
                        ad = Adv(adv_text=xml_adv_text, input_future=xml_adv_date)
                        ad.write_adv_to_file()
                        print(publish_article.attrib)
                        print(xml_adv_text)
                        print(f'{xml_adv_date}\n')
                    elif publish_article.get('name').lower() == 'joke':
                        xml_joke_text = publish_article.find('TypeData').find('Joke_Info').text
                        xml_ending = publish_article.find('TypeData').find('Ending').text
                        jk = Jokes(joke_text=xml_joke_text, ending=xml_ending)
                        jk.write_joke_to_file()
                        print(publish_article.attrib)
                        print(xml_joke_text)
                        print(f'{xml_ending}\n')
                except ValueError as e:
                    print(e)
                # print(publish_article.attrib)


class SQLite:
    def __init__(self):
        self.news_text = 'News log text '
        self.news_location = 'Cape Town'
        self.adv_text = 'ADV Text'
        self.adv_date = '2022-09-01'
        self.joke_text = 'Joke Text'
        self.ending = 'The end'
        self.connection = sqlite3.connect('test.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS news(news_text text, location text)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS adv(adv_text text, adv_date string)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS joke(joke_text text, ending text)')

    def insert_val(self):
        self.cursor.execute(f"SELECT news_text FROM news WHERE news_text = '{self.news_text}'")
        if self.cursor.fetchone() is not None:
            print('News table Duplicate check: Value is already exists')
        else:
            self.cursor.execute(f"INSERT INTO news VALUES('{self.news_text}','{self.news_location}')")

        self.cursor.execute(f"SELECT adv_text FROM adv WHERE adv_text = '{self.adv_text}'")
        if self.cursor.fetchone() is not None:
            print('Advertise table Duplicate check: Value is already exist')
        else:
            self.cursor.execute(f"INSERT INTO adv VALUES('{self.adv_text}','{self.adv_date}')")

        self.cursor.execute(f"SELECT joke_text FROM joke WHERE joke_text = '{self.joke_text}'")
        if self.cursor.fetchone() is not None:
            print('Joke table Duplicate check: Value is already exist')
        else:
            self.cursor.execute(f"INSERT INTO joke VALUES('{self.joke_text}','{self.ending}')")

        self.cursor.execute('select * from news')
        result_n = self.cursor.fetchall()
        self.cursor.execute('select * from adv')
        result_adv = self.cursor.fetchall()
        self.cursor.execute('select * from joke')
        result_j = self.cursor.fetchall()
        # print(result)
        return f"\nNews table result:{result_n}, \nAdv table result:{result_adv}, \nJoke table result:{result_j}"

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


a = SQLite()
b = a.insert_val()
print(a)
print(b)





# connection = sqlite3.connect('test.db')
# cursor = connection.cursor()
#
# cursor.execute('CREATE TABLE IF NOT EXISTS news(news_text text , location text)')
# cursor.execute('CREATE TABLE IF NOT EXISTS adv(adv_text text, adv_date string)')
#
# n_value = 'test2'
# adv_val = 'adv_test'
# cursor.execute(f"SELECT news_text FROM news WHERE news_text = '{n_value}'")
# # print(cursor.fetchone()[0])
#
# if cursor.fetchone() is not None:
#     print('Value is already exists')
# else:
#     cursor.execute(f"INSERT INTO news VALUES('{n_value}','Carribian')")
#
# cursor.execute(f"SELECT * FROM adv WHERE adv_text = '{adv_val}'")
# # print(cursor.fetchone())
# if cursor.fetchone() is not None:
#     print('ADV tables value is already exists')
# else:
#     cursor.execute(f"INSERT INTO adv VALUES('{adv_val}','2022-10-01')")
#
# connection.commit()
# cursor.execute('select * from news')
# results = cursor.fetchall()
# cursor.execute('select * from adv')
# result_adv = cursor.fetchall()
#
#
# print(results)
# print(result_adv)
# cursor.close()
# connection.close()


# connection = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};SERVER=localhost;Direct=True;DATABASE=test.db;Trusted_connection=yes')
# cursor = connection.cursor()
# cursor.execute("""
#         SELECT * FROM sqlite_master WHERE type = 'table' AND name = 'news'
#         """)
# if cursor.fetchone()[0] != None:
#     print('Table is already created')
# else:
#     cursor.execute('CREATE TABLE news(news_text text unique, location text)')
# cursor.execute("INSERT OR IGNORE INTO news VALUES('News test','Cape Town')")
# connection.commit()
# cursor.execute('select * from news')
# result = cursor.fetchall()
# print(result)
# cursor.close()
# connection.close()
