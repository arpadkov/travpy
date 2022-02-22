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
        self.villages = []

    def resource_build_available(self) -> list[Village]:
        available = []
        for village in self.villages:
            if not village.is_building_resource_field:
                available.append(village)
        return available

    def select_next_village(self):
        next_village = self.villages[0].build_until()
        for village in self.villages:
            if village.build_until() < next_village:
                next_village = village




