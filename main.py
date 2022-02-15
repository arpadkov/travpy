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


# if __name__ == '__main__':

if read_login_data():
    bot = TravianBot(read_login_data())

app = QApplication(sys.argv)

window = MainWindow(bot)
window.show()

bot.login()
bot.build_manager.ask_for_resources()


app.exec_()




# bot.refresh_resources()
# bot.run_resource_building()
# bot.build_manager.select_lowest_field(bot.resource_fields.read_fields())

# bot.exit()

