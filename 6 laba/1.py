class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def set_password(self, password):
        self.__password = password

    def check_password(self, password):
        return self.__password == password


if __name__ == '__main__':
    account = UserAccount('Lorem Ipsum', 'qwerty')
    print(account.username)
    print(account.check_password('qwerty'))

    account.set_password('1234')
    print(account.check_password('1234'))

