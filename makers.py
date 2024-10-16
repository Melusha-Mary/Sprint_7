from faker import Faker

fake = Faker()


def login_maker():
    made_login = fake.user_name()
    return made_login


def password_maker():
    made_password = fake.random_number(4)
    return made_password


def name_maker():
    made_name = fake.first_name()
    return made_name
