from page_objects.page_object import PageObject, ClickWaitWebElement
from page_objects.upgrade_resource_field_page import UpgradeResourceField
from modell.resources import Resources

from time import sleep


class Field:

    def __init__(self, element: ClickWaitWebElement):
        self.element = element
        self.outer_html = self.element.get_outer_html()

        self.field_id = self.read_id()
        self.field_level = self.read_level()
        self.field_type = self.read_type()

    def read_id(self):
        id_start = self.outer_html.find('buildingSlot')
        return int(self.outer_html[id_start+12: id_start+14])

    def read_level(self):
        return int(self.element.text())

    def read_type(self):
        type_start = self.outer_html.find('gid')
        return int(self.outer_html[type_start + 3:type_start + 5])

    def __gt__(self, other):
        return self.field_level > other.field_level

    def __eq__(self, other):
        return self.field_id == other.field_id


class ResourceFieldsPage(PageObject):

    def __init__(self):
        super(ResourceFieldsPage, self).__init__()
        self.fields = self.read_fields()

    def read_resources(self):
        lumber = self.get_element("//*[@id='l1']").text().replace(',', '')
        clay = self.get_element("//*[@id='l2']").text().replace(',', '')
        iron = self.get_element("//*[@id='l3']").text().replace(',', '')
        crop = self.get_element("//*[@id='l4']").text().replace(',', '')
        return Resources([int(lumber), int(clay), int(iron), int(crop)])

    def read_fields(self) -> list[Field]:

        self.fields = []
        field_elements = self.get_elements("//*[@class[contains(.,'buildingSlot') and contains(.,'level')]]")

        for field_element in field_elements:
            self.fields.append(Field(field_element))

        return self.fields

        # self.get_element("").hover()
        # field_name = self.get_element("//*[@class='tip-contents']//*[@class='title elementTitle']").text()

    def build_field(self, field_id_to_build):
        self.read_fields()

        for field in self.fields:
            if field.field_id == field_id_to_build:
                field.element.click()

        upgrade_page = UpgradeResourceField()

        required = upgrade_page.read_required_resources()

        if self.read_resources().is_enough_for(upgrade_page.read_required_resources()):
            upgrade_button = self.get_element("//button[contains(., 'Upgrade to level')]")
            upgrade_button.hover()

        else:
            self.get_element("//*[@class='village resourceView ']").click()



