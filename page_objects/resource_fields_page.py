from page_objects.page_object import PageObject
from page_objects.upgrade_resource_field_page import UpgradeResourceField
from modell.building import Building, BuildingConstruction
from modell.resources import Resources
from modell.field import Field
from utils.utils import building_from_string

from PyQt5 import QtCore


class MessageObject(QtCore.QObject):

    resources_signal = QtCore.pyqtSignal(object)
    fields_signal = QtCore.pyqtSignal(object)
    building_status = QtCore.pyqtSignal(object)

    def __init__(self):
        super(MessageObject, self).__init__()

    def emit_resources(self, resources: Resources):
        self.resources_signal.emit(resources)

    def emit_fields(self, fields: list[Field]):
        self.fields_signal.emit(fields)

    def emit_building_status(self, building_for: int):
        self.building_status.emit(building_for)


class ResourceFieldsPage(PageObject):

    def __init__(self):
        super(ResourceFieldsPage, self).__init__()

        self.resource_field_names = ['Woodcutter', 'Clay Pit', 'Iron Mine', 'Cropland']

        self.message_obj = MessageObject()

    def read_resources(self) -> Resources:
        lumber = self.get_element("//*[@id='l1']").text().replace(',', '')
        clay = self.get_element("//*[@id='l2']").text().replace(',', '')
        iron = self.get_element("//*[@id='l3']").text().replace(',', '')
        crop = self.get_element("//*[@id='l4']").text().replace(',', '')
        resources = Resources(int(lumber), int(clay), int(iron), int(crop))

        self.message_obj.emit_resources(resources)
        return resources

    def read_fields(self) -> list[Field]:

        fields = []
        field_elements = self.get_elements("//*[@class[contains(.,'buildingSlot') and contains(.,'level')]]")

        for field_element in field_elements:
            fields.append(Field(field_element))

        self.message_obj.emit_fields(fields)
        return fields

    def read_building_status(self):

        currently_building = self.read_currently_building()
        building_for = min(building.building_for for building in currently_building)

        self.message_obj.emit_building_status(building_for)

    def build_field(self, field_id_to_build):

        if self.is_building_resource_field():
            return

        fields = self.read_fields()

        for field in fields:
            if field.field_id == field_id_to_build:
                field.element.click()

        upgrade_page = UpgradeResourceField()

        if self.read_resources().is_enough_for(upgrade_page.read_required_resources()):
            upgrade_button = self.get_element("//button[contains(., 'Upgrade to level')]")
            upgrade_button.hover()

        else:
            self.get_element("//*[@class='village resourceView ']").click()

    def read_currently_building(self) -> list[BuildingConstruction]:
        buildings = \
            [building_from_string(b.text()) for b in self.get_elements("//*[@class='buildingList']//*[@class='name']")]

        dones_at = [done_at.value() for done_at in self.get_elements("//*[@class='buildingList']//*[@class='timer']")]

        return [BuildingConstruction(building, done_at) for (building, done_at) in zip(buildings, dones_at)]

    def is_building_resource_field(self):
        for build_under_construction in self.read_currently_building():
            if build_under_construction.get_name() in self.resource_field_names:
                return True
        return False


