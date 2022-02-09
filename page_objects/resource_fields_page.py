from page_objects.page_object import PageObject, ClickWaitWebElement

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
        return self.outer_html[type_start + 3:type_start + 5]


class ResourceFieldsPage(PageObject):

    def __init__(self):
        super(ResourceFieldsPage, self).__init__()
        self.fields = self.read_fields()

    def read_resources(self):
        lumber = self.get_element("//*[@id='l1']").text()
        clay = self.get_element("//*[@id='l2']").text()
        iron = self.get_element("//*[@id='l3']").text()
        crop = self.get_element("//*[@id='l4']").text()
        return lumber, clay, iron, crop

    def read_fields(self) -> list[Field]:

        fields = []
        field_elements = self.get_elements("//*[@class[contains(.,'buildingSlot') and contains(.,'level')]]")

        for field_element in field_elements:
            fields.append(Field(field_element))

        return fields

        # self.get_element("").hover()
        # field_name = self.get_element("//*[@class='tip-contents']//*[@class='title elementTitle']").text()

    def build_field(self, field_id_to_build):
        field_to_build = None
        for field in self.fields:
            if field.field_id == field_id_to_build:
                field_to_build = field

        if field_to_build:
            field_to_build.element.click()
            upgrade_button = self.get_element("//button[contains(., 'Upgrade to level')]")
            upgrade_button.hover()

