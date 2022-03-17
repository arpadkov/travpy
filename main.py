from gui.main_window import MainWindow
from travian_bot import TravianBot

from PyQt5.QtWidgets import QApplication

import json
import os
import sys


def read_login_data():
    if os.path.isfile(os.path.join(os.getenv('APPDATA'), 'travpy', 'login.json')):
        with open(os.path.join(os.getenv('APPDATA'), 'travpy', 'login.json')) as file:
            json_data = json.load(file)
    return json_data["server_url"], json_data["username"], json_data["password"]


bot = TravianBot(read_login_data())

app = QApplication(sys.argv)

window = MainWindow(bot)
window.show()

bot.login()
bot.initialize_villages()
print(bot.task_manager.villages[0].next_resource_task_available_at)

app.exec_()


