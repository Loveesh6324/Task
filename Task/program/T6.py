from csv import DictReader
import pymysql

connection = pymysql.connect(
    host="localhost", port=3306, user="root", passwd="", database="test")
cursor = connection.cursor()

with open('username.csv', mode='r') as file:

    dict1 = DictReader(file)
    list_dict1 = list(dict1)


test1 = """CREATE TABLE Test1(
USERNAME Varchar(20),
IDENTIFIER Varchar(10),
FIRSTNAME  VARCHAR(20),
LASTNAME VARCHAR(20))"""

cursor.execute(test1)

for d in list_dict1:
    data1 = tuple([i for i in d.values()])
    cursor.execute(
        "INSERT INTO Test1 (USERNAME, IDENTIFIER, FIRSTNAME, LASTNAME) VALUES(%s,%s,%s,%s);", data1)

connection.commit()
