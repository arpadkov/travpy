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
        self.next_resource_task_available_at = datetime.datetime
        self.village_name = str

        self.initialize_village()

    def initialize_village(self):
        village_elements = self.resource_fields.get_elements("//*[@class='villageList']//*[@class='iconAndNameWrapper']")
        self.village_name = village_elements[self.village_num].text()
        village_elements[self.village_num].click()

        self.build_manager.ask_building_status()
        self.build_manager.ask_for_fields()
        self.build_manager.ask_for_resources()

        self.is_building_resource_field = self.resource_fields.is_building_resource()

        self.set_next_resource_task()

    def connect_build_manager_to_resource_fields(self):
        self.build_manager.ask_building_status_signal.connect(self.resource_fields.read_resource_building_status)
        self.resource_fields.resource_building_status.connect(self.build_manager.set_building_status)

        self.build_manager.ask_resources_signal.connect(self.resource_fields.read_resources)
        self.resource_fields.resources_signal.connect(self.build_manager.set_resources)

        self.build_manager.ask_fields_signal.connect(self.resource_fields.read_fields)
        self.resource_fields.fields_signal.connect(self.build_manager.set_fields)

        self.build_manager.build_resource_field_signal.connect(self.resource_fields.build_field)

    def build_until(self):
        return self.build_manager.building_until

    def resource_fields_completed(self) -> bool:
        """
        bug for main village: if all resource fields are AT level 10, the bot will think, that it is completed
        """
        for resource_field in self.build_manager.fields:
            if resource_field.field_level != 10:
                return False
        return True

    def set_next_resource_task(self):
        self.next_resource_task_available_at =\
            datetime.datetime.now() + self.resource_fields.read_resource_building_status()
        # print(self.next_resource_task_available_at)

    def emit_building_done_at_signal(self):
        self.building_done_at_signal.emit(self.build_manager.building_until)

    def __repr__(self):
        return f'Village: {self.village_name}'
