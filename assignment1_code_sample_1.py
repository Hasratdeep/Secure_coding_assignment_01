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

def get_data():
    url = 'http://insecure-api.com/get-data'
    if not url.startswith("https://"):
        print("Error: Failed to load Url.")
        return None
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')")
        connection.commit()
        print("Data Successfully saved.")
    except Exception as e:
        print("Error:", e)
        cursor.close()
        connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
