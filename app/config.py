# # Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# # Чтобы добавить новую настройку, допишите ее в класс.


class Config(object):
    DEBUG = True
    SECRET = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False