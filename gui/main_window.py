from gui.console import ConsoleWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton

from travian_bot import TravianBot


class MainWindow(QMainWindow):
    def __init__(self, bot: TravianBot):
        super().__init__()

        self.bot = bot

        self.console = ConsoleWidget()

        self.console.push_vars({"bot": self.bot, "villages": self.bot.task_manager.villages})

        self.setWindowTitle('TravianBot')

        # Set the central widget of the Window.
        self.setCentralWidget(self.console)

    def closeEvent(self, event):
        self.bot.close()




