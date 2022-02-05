from LoginPage import LoginPage


class TravianBot:

    def __init__(self):

        self.login_page = LoginPage('xyzkds', 'Emiatyuk95')

    def login(self):
        self.dorf1_page = self.login_page.get_dorf1_page()





if __name__ == '__main__':
    bot = TravianBot()

    bot.login()


