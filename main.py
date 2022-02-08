from travian_bot import TravianBot

import json
import os


def read_login_data():
    if os.path.isfile(os.path.join(os.getenv('APPDATA'), 'travpy', 'login.json')):
        with open(os.path.join(os.getenv('APPDATA'), 'travpy', 'login.json')) as file:
            json_data = json.load(file)
    return json_data["server_url"], json_data["username"], json_data["password"]


if __name__ == '__main__':

    if read_login_data():
        bot = TravianBot(read_login_data())

    bot.login()

    print(bot.resource_fields.resources)

    bot.exit()


