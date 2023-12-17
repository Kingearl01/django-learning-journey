from django.contrib.auth.hashers import make_password, PBKDF2SHA1PasswordHasher
import csv

def generate_password():
    with open('hall4l100.csv') as file:
        csv_reader = csv.reader(file)
        with open('users-l100.csv', 'w+', newline='') as user_file:
            user_writer = csv.writer(user_file)
            for row in csv_reader:
                pswd = str(row[3])
                user_writer.writerow(make_password(pswd))
                print(f'{type(pswd)} -- {pswd}')

        file.close()


generate_password()