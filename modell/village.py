from page_objects.resource_fields_page import ResourceFieldsPage
from modell.build_manager import BuildManager

from PyQt5 import QtCore
import datetime


class Village(QtCore.QObject):

    def __init__(self, village_num: int):
        super(Village, self).__init__()

        self.village_num = village_num

        self.resource_fields = ResourceFieldsPage()
        self.build_manager = BuildManager()

        self.connect_build_manager_to_resource_fields()

        self.is_building_resource_field = bool

        self.village_name = ''
        self.initialize_village()

    def initialize_village(self):
        village_elements = self.resource_fields.get_elements("//*[@class='villageList']//*[@class='iconAndNameWrapper']")
        self.village_name = village_elements[self.village_num].text()
        village_elements[self.village_num].click()

        self.build_manager.ask_building_status()
        self.build_manager.ask_for_fields()
        self.build_manager.ask_for_resources()

        self.is_building_resource_field = self.resource_fields.is_building_resource_field()

    def connect_build_manager_to_resource_fields(self):
        self.build_manager.ask_building_status_signal.connect(self.resource_fields.read_building_status)
        self.resource_fields.building_status.connect(self.build_manager.set_building_status)

        self.build_manager.ask_resources_signal.connect(self.resource_fields.read_resources)
        self.resource_fields.resources_signal.connect(self.build_manager.set_resources)

        self.build_manager.ask_fields_signal.connect(self.resource_fields.read_fields)
        self.resource_fields.fields_signal.connect(self.build_manager.set_fields)

        self.build_manager.build_resource_field_signal.connect(self.resource_fields.build_field)

    def build_until(self):
        return self.build_manager.building_until

    def emit_building_done_at_signal(self):
        self.building_done_at_signal.emit(self.build_manager.building_until)

    def __repr__(self):
        return f'Village: {self.village_name}'
