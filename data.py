import random

class Credential:
    email = 'danil_novyh_34_123@yandex.ru'
    password = 'danil_novyh_34_123'

timeout = 20


class TestData:
    @staticmethod
    def generate_email():
        return f"auto_test_{random.randint(100000, 999999)}@yandex.ru"

    @staticmethod
    def generate_password():
        return f"SecurePass{random.randint(1000, 9999)}!"