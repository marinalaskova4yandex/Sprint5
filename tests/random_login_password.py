from faker import Faker

fake = Faker()

#  Функция создания логина
def generate_fake_email(domain="yandex.ru"):
    username = fake.user_name()
    email = f"{username}@{domain}"
    print(f"Сгенерирован логин (email): {email}")
    return email
    
#  Функция создания пароля
def generate_fake_password(min_length=6):
    password = fake.password(length=max(6, min_length))
    print(f"Сгенерирован пароль: {password}")
    return password