from page_objects.login_page import LoginPage
from modell.resource_fields import ResourceFields


class TravianBot:

    def __init__(self, login_data):

        self.login_page = LoginPage(login_data)
        self.resource_fields = ResourceFields

    def login(self):
        self.resource_fields = ResourceFields(self.login_page.get_resource_fields_page())

    def run_resource_building(self):


    def exit(self):
        self.login_page.close_browser()
