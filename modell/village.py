from page_objects.resource_fields_page import ResourceFieldsPage
from modell.build_manager import BuildManager


class Village:

    def __init__(self):
        self.resource_fields = ResourceFieldsPage()
        self.build_manager = BuildManager()

    def connect_build_manager_to_resource_fields(self):
        self.build_manager.message_obj.ask_building_status.connect(self.resource_fields.read_building_status)
        self.resource_fields.message_obj.building_status.connect(self.build_manager.set_building_status)

        self.build_manager.message_obj.ask_resources_signal.connect(self.resource_fields.read_resources)
        self.resource_fields.message_obj.resources_signal.connect(self.build_manager.set_resources)

        self.build_manager.message_obj.ask_fields_signal.connect(self.resource_fields.read_fields)
        self.resource_fields.message_obj.fields_signal.connect(self.build_manager.set_fields)

        self.build_manager.message_obj.build_resource_field_signal.connect(self.resource_fields.build_field)
