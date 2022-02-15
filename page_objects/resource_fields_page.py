from page_objects.page_object import PageObject
from page_objects.upgrade_resource_field_page import UpgradeResourceField
from modell.resources import Resources
from modell.field import Field

from PyQt5 import QtCore

from time import sleep


class MessageObject(QtCore.QObject):

    resources_signal = QtCore.pyqtSignal(object)
    fields_signal = QtCore.pyqtSignal(object)

    def __init__(self):
        super(MessageObject, self).__init__()

    def emit_resources(self, resources: Resources):
        self.resources_signal.emit(resources)

    def emit_fields(self, fields: list[Field]):
        self.fields_signal.emit(fields)


class ResourceFieldsPage(PageObject):

    def __init__(self):
        super(ResourceFieldsPage, self).__init__()
        # self.fields = []

        self.message_obj = MessageObject()

    def read_resources(self):
        lumber = self.get_element("//*[@id='l1']").text().replace(',', '')
        clay = self.get_element("//*[@id='l2']").text().replace(',', '')
        iron = self.get_element("//*[@id='l3']").text().replace(',', '')
        crop = self.get_element("//*[@id='l4']").text().replace(',', '')
        resources = Resources([int(lumber), int(clay), int(iron), int(crop)])

        self.message_obj.emit_resources(resources)
        return resources

    def read_fields(self) -> list[Field]:

        fields = []
        field_elements = self.get_elements("//*[@class[contains(.,'buildingSlot') and contains(.,'level')]]")

        for field_element in field_elements:
            fields.append(Field(field_element))

        self.message_obj.emit_fields(fields)
        return fields

        # self.get_element("").hover()
        # field_name = self.get_element("//*[@class='tip-contents']//*[@class='title elementTitle']").text()

    def build_field(self, field_id_to_build):
        fields = self.read_fields()

        for field in fields:
            if field.field_id == field_id_to_build:
                field.element.click()

        upgrade_page = UpgradeResourceField()

        # required = upgrade_page.read_required_resources()

        if self.read_resources().is_enough_for(upgrade_page.read_required_resources()):
            upgrade_button = self.get_element("//button[contains(., 'Upgrade to level')]")
            upgrade_button.hover()

        else:
            self.get_element("//*[@class='village resourceView ']").click()



