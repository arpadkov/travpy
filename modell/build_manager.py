from page_objects.resource_fields_page import Field
from modell.resources import Resources

from PyQt5 import QtCore

import datetime


class BuildManager(QtCore.QObject):

    ask_resources_signal = QtCore.pyqtSignal()
    ask_fields_signal = QtCore.pyqtSignal()
    ask_building_status_signal = QtCore.pyqtSignal()

    build_resource_field_signal = QtCore.pyqtSignal(object)

    def __init__(self):
        super(BuildManager, self).__init__()

        self.resources = Resources()
        self.fields = list[Field]

        self.building_until = datetime.datetime

    def ask_for_resources(self):
        self.ask_resources_signal.emit()

    def ask_for_fields(self):
        self.ask_fields_signal.emit()

    def ask_building_status(self):
        self.ask_building_status_signal.emit()

    def set_resources(self, resources: Resources):
        self.resources = resources

    def set_fields(self, fields: list[Field]):
        self.fields = fields

    def set_building_status(self, building_for: datetime.timedelta):
        self.building_until = datetime.datetime.now() + building_for

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

    def build_resource_field(self, field_id: int):
        self.build_resource_field_signal.emit(field_id)
