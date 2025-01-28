import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from ui_manager import UIManager


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        loadUi("ui\main_window.ui", self)
        self.ui_manager = UIManager(self)

        self.load_styles()

    def load_styles(self):
        with open("styles/styles.qss", "r") as file:
            self.setStyleSheet(file.read())

    def closeEvent(self, event):
        self.ui_manager.save_players()
        event.accept()

    def on_actionLoad_triggered(self):
        if self.ui_manager:
            self.ui_manager.load_saved_players()
        else:
            print("UIManager not found in MainWindow.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
