from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class PageObject:

    def __init__(self, timeout=5):

        self.driver = webdriver.Chrome()

        self.timeout = timeout

    def get_element(self, xpath):
        element_present = expected_conditions.presence_of_element_located((By.XPATH, xpath))
        element = WebDriverWait(self.driver, self.timeout).until(element_present)
        return element
