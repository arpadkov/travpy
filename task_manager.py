import datetime

from modell.village import Village
from PyQt5 import QtCore

import time


class BuildThread(QtCore.QThread):

    building_pulse_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(BuildThread, self).__init__()

    def run(self):
        while True:
            time.sleep(3)
            self.building_pulse_signal.emit()


class TaskManager:

    def __init__(self):
        self.villages = list[Village]

    def resource_build_available(self) -> list[Village]:
        available = []
        for village in self.villages:
            if not village.is_building_resource_field and not village.resource_fields_completed():
                available.append(village)
        return available

    def select_next_village(self):
        """
        DO NOT USE, makes no sense
        """
        next_village = self.villages[0]

        for village in self.villages:
            if village.build_until() < next_village.build_until():
                next_village = village
        return next_village

    def select_next_resource_task(self) -> (Village, datetime.datetime):
        next_village_for_resource = self.villages[0]








