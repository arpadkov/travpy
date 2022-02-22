from page_objects.page_object import PageObject


class LoginPage(PageObject):

    def __init__(self, login_data):
        super(LoginPage, self).__init__()
        self.server_url, self.username, self.password = login_data

    def enter_login_data(self):
        self.get_element("//input[@name='name']").send_keys(self.username)
        self.get_element("//input[@name='password']").send_keys(self.password)

    def login(self):
        self.driver.get(self.server_url)
        self.enter_login_data()
        self.get_element("//button[@value='Login']").click()

    def close_browser(self):
        self.driver.close()
