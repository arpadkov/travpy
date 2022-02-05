from PageObject import PageObject


class LoginPage(PageObject):

    def __init__(self, username, password):
        super(LoginPage, self).__init__()

        self.username = username
        self.password = password

    def accept_cookies(self):
        try:
            cookie_button = self.get_element('//*[@id="cmpwelcomebtnyes"]/a')
            cookie_button.Click()
        except Exception as e:
            print(e)

    def enter_login_data(self):
        self.get_element("//input[@name='name']").send_keys(self.username)
        self.get_element("//input[@name='password']").send_keys(self.password)



    def get_dorf1_page(self):

        self.driver.get('https://ts2.x1.europe.travian.com/')

        # self.accept_cookies()

        self.enter_login_data()

        self.get_element("//button[@value='Login']").click()
