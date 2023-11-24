from pandas import *
import random
import array
import boto3
import pandas as pd
import time


def r_pass():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?',
               '.', '/', '|', '~', '>', '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    randompassword = ""
    for x in temp_pass_list:
        randompassword = randompassword + x

    return randompassword


def r_user():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)

    temp_pass = rand_digit + rand_upper + rand_lower

    return "User-"+temp_pass


def create_user():

    temp_user = r_user()
    temp_pass = r_pass()
    iam.create_user(
        UserName=temp_user
    )

    iam.add_user_to_group(
        GroupName='test-group',
        UserName=temp_user
    )

    iam.create_login_profile(
        UserName=temp_user,
        Password=temp_pass
    )
    return(temp_user, temp_pass)


def delete_user():

    for i in range(len(cred)):

        iam.delete_login_profile(
            UserName=cred[i]
        )

        iam.remove_user_from_group(
            GroupName='test-group',
            UserName=cred[i]
        )

        iam.delete_user(
            UserName=cred[i]
        )


iam = boto3.client(
    service_name='iam',
    region_name='ap-south-1',
    aws_access_key_id='AKIAUKKU4CXXNZKXTUFP',
    aws_secret_access_key='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'
)

lst = []
feild = ['Username', 'Password']
n = int(input("Enter number of Users you wish to Create:"))

for i in range(n):
    dict = {}
    user, passwrd = create_user()
    dict['Username'] = user
    dict['Password'] = passwrd
    lst.append(dict)
ss = pd.DataFrame(lst)
ss.to_csv('User_details.csv')

data = read_csv('User_details.csv')
cred = data['Username'].tolist()
print(cred)

while True:
    time.sleep(20)
    delete_user()
    print("User Deleted Successfully")
    break
