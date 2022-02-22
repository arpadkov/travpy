from page_objects.resource_fields_page import Field
from modell.resources import Resources

from PyQt5 import QtCore

import time


class MessageObject(QtCore.QObject):

    ask_resources_signal = QtCore.pyqtSignal()
    ask_fields_signal = QtCore.pyqtSignal()
    ask_building_status = QtCore.pyqtSignal()

    build_resource_field_signal = QtCore.pyqtSignal(object)

    def __init__(self):
        super(MessageObject, self).__init__()

    def emit_ask_resources(self):
        self.ask_resources_signal.emit()

    def emit_ask_fields(self):
        self.ask_fields_signal.emit()

    def emit_ask_building_status(self):
        self.ask_building_status.emit()

    def build_resource_field(self, field_id: int):
        self.build_resource_field_signal.emit(field_id)


class BuildThread(QtCore.QThread):

    building_pulse_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(BuildThread, self).__init__()

    def run(self):
        while True:
            time.sleep(3)
            print('Sending build signal')
            self.building_pulse_signal.emit()


class BuildManager:

    def __init__(self):
        self.resources = Resources()
        self.fields = []

        self.building_until = None

        self.build_thread = BuildThread()

        self.message_obj = MessageObject()

        self.build_thread.building_pulse_signal.connect(self.build_lowest_resource_field)

    def ask_for_resources(self):
        self.message_obj.emit_ask_resources()

    def ask_for_fields(self):
        self.message_obj.emit_ask_fields()

    def ask_building_status(self):
        self.message_obj.emit_ask_building_status()

    def set_resources(self, resources: Resources):
        self.resources = resources

    def set_fields(self, fields: list[Field]):
        self.fields = fields

    def set_building_status(self, building_for: int):
        # TODO: convert it to datetime
        self.building_until = building_for
        print(self.building_until)

    def run_resource_building(self):
        self.build_thread.start()

    def build_lowest_resource_field(self):
        build_id = self.select_field_to_build()
        self.message_obj.build_resource_field(build_id)

    def select_field_to_build(self) -> int:
        self.ask_for_resources()
        self.ask_for_fields()

        resource = self.resources.lowest()

        identical_fields = []
        for field in self.fields:
            if resource == field.field_type:
                identical_fields.append(field)

        lowest_level_field = min(identical_fields)
        return lowest_level_field.field_id

