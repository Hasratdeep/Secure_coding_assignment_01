import os
import pymysql  # type: ignore
from urllib.request import urlopen

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': os.getenv('db_password')
}

def get_user_input():
    user_input = input('Enter your name: ')
    if user_input.strip():
        return user_input
    else:
        print("Please enter letters only, no symbols or numbers.")
        return None

def send_email(to, subject, body):
    print("To:", to)
    print("Subject:", subject)
    print("Body:", body)
    print("Email sent successfully.")
    send_email("xyz@example.com", "Welcome!", "Hello, this is a greetings email.")

def get_data():
    url = 'https://insecure-api.com/get-data'
    if not url.startswith("https://"):
        print("Error: Failed to load Url.")
        return None
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO mytable (column1, column2)
            VALUES (%(data)s, %(value)s)
        """, {
            'data': data,
            'value': "Another Value"
        })
    try:
        connection.commit()
        print("Data Successfully saved.")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
