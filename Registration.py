# Login должен содержать только латинские буквы, цифры и знак подчеркивания.
# Длина login должна быть меньше 20 символов. Если login не соответствует этим требованиям, необходимо выбросить
# WrongLoginException.
# Password должен содержать только латинские буквы, цифры и знак подчеркивания.
# Длина password должна быть меньше 20 символов. Также password и confirmPassword должны быть равны.
# Если password не соответствует этим требованиям, необходимо выбросить WrongPasswordException.
# WrongPasswordException и WrongLoginException – пользовательские (кастомные) классы исключения с конструктором,
# который принимает сообщение исключения и передает его в конструктор класса Exception (предусмотреть вызов
# данного исключения без сообщения). Обработка исключений проводится внутри метода. Используем multi-except block.
# Метод возвращает True, если значения верны или False в другом случае.

import re


class RegistrationException(Exception):
    def __init__(self, message):  # todo None подумай и разберись!
        super().__init__(message)


class WrongPasswordException(RegistrationException):
    pass


class WrongLoginException(RegistrationException):
    pass


class Registration:

    @staticmethod
    def validity(user_string):
        if re.match(r"^\b\w+\b$", user_string, flags=re.ASCII | re.MULTILINE) and len(user_string) < 20:
            return True
        else:
            return False

    @staticmethod
    def basic_check(user_login, user_password, user_confirm_password):
        # check = False
        if not Registration.validity(user_login):
            raise WrongLoginException("Login must include Aa-Zz_ only and be less than 20 char!")
        elif not Registration.validity(user_password):
            raise WrongPasswordException("Password must include Aa-Zz_ only and be less than 20 char!")
        elif user_confirm_password != user_password:
            raise WrongPasswordException("Passwords don't match!")

    @staticmethod
    def validity_check(t_login, t_password, t_confirm_password):
        try:
            Registration.basic_check(t_login, t_password, t_confirm_password)
        except WrongLoginException as exs:
            print(exs)
        except WrongPasswordException as exs:
            print(exs)
        else:
            # login, password, confirm_password = t_login, t_password, t_confirm_password
            # я понял что это не нужно потому что метод статический, эти переменные никуда не пойдут
            print("all good!")
