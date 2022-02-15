from gui.console import ConsoleWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, bot):
        super().__init__()

        self.bot = bot

        self.console = ConsoleWidget()

        self.console.push_vars({"bot": self.bot})

        self.setWindowTitle('TravianBot')

        # Set the central widget of the Window.
        self.setCentralWidget(self.console)

    def closeEvent(self, event):
        self.bot.close()




