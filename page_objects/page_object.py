from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from random import randint
from time import sleep


def random_sleep():
    sleep(randint(1, 1000)/1000)


class PageObject:

    driver = webdriver.Chrome()

    def __init__(self, timeout=5):
        self.timeout = timeout

    def get_element(self, xpath):
        element_present = expected_conditions.presence_of_element_located((By.XPATH, xpath))
        element = WebDriverWait(self.driver, self.timeout).until(element_present)
        return ClickWaitWebElement(element)


class ClickWaitWebElement:
    """
    Wrapper for WebElement object of selenium
    for any action the random_sleep function is called
    """

    def __init__(self, web_element: WebElement):
        self._web_element = web_element

    def click(self):
        random_sleep()
        self._web_element.click()

    def send_keys(self, keys: str):
        random_sleep()
        self._web_element.send_keys(keys)

    def text(self):
        return self._web_element.text
