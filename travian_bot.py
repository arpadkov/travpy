from page_objects.login_page import LoginPage


class TravianBot:

    def __init__(self, login_data):

        self.login_page = LoginPage(login_data)

    def login(self):
        self.login_page.get_dorf1_page()
