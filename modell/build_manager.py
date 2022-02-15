from page_objects.resource_fields_page import Field
from modell.resources import Resources

from PyQt5 import QtCore

import time


class MessageObject(QtCore.QObject):

    ask_resources_signal = QtCore.pyqtSignal()
    ask_fields_signal = QtCore.pyqtSignal()

    build_resource_field_signal = QtCore.pyqtSignal(object)

    def __init__(self):
        super(MessageObject, self).__init__()

    def emit_ask_resources(self):
        self.ask_resources_signal.emit()

    def emit_ask_fields(self):
        self.ask_fields_signal.emit()

    def build_resource_field(self, field_id: int):
        self.build_resource_field_signal.emit(field_id)


class BuildThread(QtCore.QThread):

    def __init__(self):
        super(BuildThread, self).__init__()

    def run(self):
        while True:
            pass


class BuildManager:

    def __init__(self):
        self.resources = Resources
        self.fields = []

        self.message_obj = MessageObject()

    def ask_for_resources(self):
        self.message_obj.emit_ask_resources()

    def ask_for_fields(self):
        self.message_obj.emit_ask_fields()

    def set_resources(self, resources: Resources):
        self.resources = resources

    def set_fields(self, fields: list[Field]):
        self.resources = fields

    def run_resource_building(self):
        build_id = self.select_field_to_build()
        self.message_obj.build_resource_field(build_id)

    def select_lowest_resource(self):
        # TODO: refactor to use built in method of Resources object
        resource_list = self.resources.as_list()
        lowest_value = min(resource_list)
        return resource_list.index(lowest_value) + 1

    def select_lowest_field(self, fields: list[Field]):
        resource_index = self.select_lowest_resource()

        identical_fields = []
        for field in fields:
            if resource_index == field.field_type:
                identical_fields.append(field)

        lowest_level_field = min(identical_fields)
        return lowest_level_field.field_id

    def select_field_to_build(self):

        self.ask_for_resources()
        self.ask_for_fields()

        # self.refresh_resources(resources)
        # lowest_resource_id = self.select_lowest_resource()
        field_id = self.select_lowest_field(fields)
        return field_id


