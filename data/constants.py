import os

class Constants:
    try:
        login = os.getenv('AUTH_LOGIN')
        passwrod = os.getenv('AUTH_PASSWORD')
    except KeyError:
        print('LOGIN OR PW WASNT FOUNT')

