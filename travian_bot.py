from page_objects.login_page import LoginPage
from modell.village import Village
from task_manager import TaskManager


class TravianBot:

    def __init__(self, login_data):
        self.login_page = LoginPage(login_data)

        self.task_manager = TaskManager()

    def login(self):
        self.login_page.login()

    def refresh_villages(self):

        self.task_manager.villages.clear()
        villages_num = len(self.login_page.get_elements("//*[@class='villageList']//*[@class='iconAndNameWrapper']"))
        for village_num in range(villages_num):
            self.task_manager.villages.append(Village(village_num))

    def close(self):
        self.login_page.close_browser()

    def __del__(self):
        self.login_page.close_browser()
