from faker import Faker

fake = Faker()

#  1. Функция создания логина
def generate_fake_email(domain="yandex.ru"):
    username = fake.user_name()
    email = f"{username}@{domain}"
    return email
    
#  2. Функция создания пароля
def generate_fake_password(min_length=6):
    password = fake.password(length=max(6, min_length))
    return password