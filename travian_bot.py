from page_objects.login_page import LoginPage
from modell.village import Village


class TravianBot:

    def __init__(self, login_data):
        self.login_page = LoginPage(login_data)

        self.villages = []

    def login(self):
        self.login_page.login()

    def initialize_villages(self):

        villages_num = len(self.login_page.get_elements("//*[@class='villageList']//*[@class='iconAndNameWrapper']"))
        for village_num in range(villages_num):
            self.villages.append(Village(village_num))

    def close(self):
        self.login_page.close_browser()

    def __del__(self):
        self.login_page.close_browser()
