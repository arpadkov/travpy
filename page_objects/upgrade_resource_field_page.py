from page_objects.page_object import PageObject, ClickWaitWebElement
from modell.resources import Resources


class UpgradeResourceField(PageObject):

    def __init__(self):
        super(UpgradeResourceField, self).__init__()

        self.required = self.read_required_resources()

    def read_required_resources(self):
        icons = self.get_elements("//*[@class='inlineIcon resource']")
        return Resources([icon.text() for icon in icons][0:4])


