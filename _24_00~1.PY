import re
import datetime as dt
import os, random, smtplib

# Constants:
PATH_TO_CSV_FILE = "data/birthdays.csv"
date_pattern = r'(\d{4}),\s*(\d{1,2}),\s*(\d{1,2})'
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
each_row_format_pattern = r'([^,]+),\s*(' + email_pattern + r'),\s*' + date_pattern

# Functions:

# email sending function:
def send_a_gmail_email(their_email2, name, letter_content):
    my_email1 = os.environ.get('my_email1')  # the API Key from the open weather website
    print(f"my_email1 is: {my_email1}")

    password = os.environ.get('password')  # the API Key from the open weather website
    print(f"password is: {password}")

    that_other_email3 = os.environ.get('that_other_email3')  # the API Key from the open weather website
    print(f"that_other_email3 is: {that_other_email3}")

    subject = f"Subject: Happy Birthday {name}!\n\n"
    body = letter_content.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email1, password=password)
        connection.sendmail(from_addr=my_email1, to_addrs=their_email2, msg=f"{subject}{body}")

# reading CSV file and populate dictionary:
data_dictionary = {}
with open(PATH_TO_CSV_FILE, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        row_match = re.search(each_row_format_pattern, line)
        if row_match:
            name, email, bd_year, bd_month, bd_day = row_match.groups()
            data_dictionary[line_number] = (name, (bd_year, bd_month, bd_day), email)

# find and read .txt letter templates:
letters_directory = "data/letter_templates"
scanned_and_indexed_letters = {}
for i, filename in enumerate(os.listdir(letters_directory)):
    with open(os.path.join(letters_directory, filename), 'r') as file:
        scanned_and_indexed_letters[i] = file.read()

# check for today's birthdays
now = dt.datetime.now()
for line_number, (name, (bd_year, bd_month, bd_day), email) in data_dictionary.items():
    if int(bd_month) == now.month and int(bd_day) == now.day:
        print(f"{name} (line #{line_number}) has a birthday today! Email: {email}")
        random_index = random.choice(list(scanned_and_indexed_letters.keys()))
        random_letter = scanned_and_indexed_letters[random_index]
        send_a_gmail_email(email, name, random_letter)    # Gets passed into: (their_email2, name, letter_content):
        # break   # use break only IF you want it to stop after it found 1 matching birthday

