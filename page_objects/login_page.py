from page_objects.page_object import PageObject
from page_objects.resource_fields_page import ResourceFieldsPage


class LoginPage(PageObject):

    def __init__(self, login_data):
        super(LoginPage, self).__init__()

        self.server_url, self.username, self.password = login_data

    def accept_cookies(self):
        try:
            cookie_button = self.get_element('//*[@id="cmpwelcomebtnyes"]/a')
            cookie_button.Click()
        except Exception as e:
            print(e)

    def enter_login_data(self):
        self.get_element("//input[@name='name']").send_keys(self.username)
        self.get_element("//input[@name='password']").send_keys(self.password)

    def get_resource_fields_page(self):

        self.driver.get(self.server_url)

        # self.accept_cookies()

        self.enter_login_data()

        self.get_element("//button[@value='Login']").click()

        return ResourceFieldsPage()

    def close_browser(self):
        self.driver.close()
