from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from random import randint
from time import sleep


def random_sleep():
    sleep(randint(1, 1000)/1000)


class ClickWaitWebElement:
    """
    Wrapper for WebElement object of selenium
    for any action the random_sleep function is called
    """

    def __init__(self, web_element: WebElement, driver):
        self._web_element = web_element
        self.driver = driver

    def click(self):
        random_sleep()
        self._web_element.click()

    def send_keys(self, keys: str):
        random_sleep()
        self._web_element.send_keys(keys)

    def hover(self):
        ActionChains(self.driver).move_to_element(self._web_element).perform()
        sleep(1)

    def text(self):
        return self._web_element.text

    def get_inner_html(self) -> str:
        return self._web_element.get_attribute('innerHTML')

    def get_outer_html(self) -> str:
        return self._web_element.get_attribute('outerHTML')


class PageObject:

    driver = webdriver.Chrome()

    def __init__(self, timeout=5):
        self.timeout = timeout

    def get_element(self, xpath):
        element_present = expected_conditions.presence_of_element_located((By.XPATH, xpath))
        element = WebDriverWait(self.driver, self.timeout).until(element_present)
        return ClickWaitWebElement(element, self.driver)

    def get_elements(self, path) -> list[ClickWaitWebElement]:
        web_elements = self.driver.find_elements_by_xpath(path)
        my_web_elements = []
        for web_element in web_elements:
            my_web_elements.append(ClickWaitWebElement(web_element, self.driver))
        return my_web_elements







