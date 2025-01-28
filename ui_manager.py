from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QFileDialog, QAction
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from modules.storage_manager import StorageManager
from modules.attributes.attributeManager import AttributeManager


class PlayerItem(QFrame):
    # Represents a single player card in the UI.

    def __init__(self, parent=None, attributes={}, ui_manager=None):
        super(PlayerItem, self).__init__(parent)
        loadUi("ui/player_item.ui", self)  # Load UI
        self.setFixedSize(250, 75)

        self.attributes = attributes
        self.ui_manager = ui_manager

        self.firstNameBox.setText(attributes.get("first_name", ""))
        self.lastNameBox.setText(attributes.get("last_name", ""))
        self.positionBox.setText(attributes.get("position", ""))

        self.mousePressEvent = self.select_player

    def select_player(self, event):
        if self.ui_manager:
            self.ui_manager.set_selected_player(self)

    def update_ui(self):
        self.firstNameBox.setText(self.attributes.get("first_name", ""))
        self.lastNameBox.setText(self.attributes.get("last_name", ""))
        self.positionBox.setText(self.attributes.get("position", ""))
        AttributeManager.apply_attributes(self, self.attributes)

    def get_player_data(self):
        return self.attributes


class PlayerContainer(QFrame):
    # container that adds space around PlayerItem

    def __init__(self, parent=None, attributes={}, ui_manager=None):
        super(PlayerContainer, self).__init__(parent)
        self.setFixedSize(280, 100)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setAlignment(Qt.AlignCenter)

        self.player_item = PlayerItem(self, attributes, ui_manager)
        layout.addWidget(self.player_item)
        AttributeManager.apply_attributes(self, attributes)

    def get_player_data(self):
        return {
            "first_name": self.attributes.get("first_name", self.firstNameBox.text()),
            "last_name": self.attributes.get("last_name", self.lastNameBox.text()),
            "position": self.attributes.get("position", self.positionBox.text()),
            "captaincy": self.attributes.get("captaincy", "None"),
            "playing_time": self.attributes.get("playing_time", "None"),
            "contract": self.attributes.get("contract", "None"),
            "foreign": self.attributes.get("foreign", False),
            "youth": self.attributes.get("youth", False),
            "injury": self.attributes.get("injury", False)
        }


class UIManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.player_list = main_window.findChild(QWidget, "playerCardList")
        self.player_list_layout = QVBoxLayout()
        self.player_list.setLayout(self.player_list_layout)

        self.selected_player = None
        self.main_window.ui_manager = self
        self.load_action = main_window.findChild(QAction, "actionLoad")

        if hasattr(main_window, "actionLoad"):
            try:
                main_window.actionLoad.triggered.disconnect()
            except TypeError:
                pass

            main_window.actionLoad.triggered.connect(self.load_saved_players)
        else:
            print("actionLoad not found in MainWindow.")

        # Find customization container elements
        self.first_name_input = main_window.findChild(QWidget, "firstNameBox")
        self.last_name_input = main_window.findChild(QWidget, "lastNameBox")
        self.position_input = main_window.findChild(QWidget, "position_box")
        self.captaincy_dropdown = main_window.findChild(
            QWidget, "captaincyBox")
        self.playing_time_dropdown = main_window.findChild(
            QWidget, "playingTimeBox")
        self.contract_dropdown = main_window.findChild(QWidget, "contractBox")
        self.foreign_checkbox = main_window.findChild(
            QWidget, "foreignCheckbox")
        self.youth_checkbox = main_window.findChild(QWidget, "youthCheckbox")
        self.injury_checkbox = main_window.findChild(QWidget, "injuryCheckbox")

        # Connect signals for updating player attributes
        self.first_name_input.textChanged.connect(self.update_selected_player)
        self.last_name_input.textChanged.connect(self.update_selected_player)
        self.position_input.textChanged.connect(self.update_selected_player)
        self.captaincy_dropdown.currentTextChanged.connect(
            self.update_selected_player)
        self.playing_time_dropdown.currentTextChanged.connect(
            self.update_selected_player)
        self.contract_dropdown.currentTextChanged.connect(
            self.update_selected_player)
        self.foreign_checkbox.stateChanged.connect(self.update_selected_player)
        self.youth_checkbox.stateChanged.connect(self.update_selected_player)
        self.injury_checkbox.stateChanged.connect(self.update_selected_player)

        main_window.addPlayerButton.clicked.connect(self.add_player)

    def set_selected_player(self, player_item):
        if self.selected_player:
            self.selected_player.setStyleSheet("")

        self.selected_player = player_item
        self.selected_player.setStyleSheet(
            "border: 2px solid lightblue;")  # Highlight

        attributes = self.selected_player.get_player_data()

        # Block signals before updating UI fields (prevents auto-triggering update_selected_player)
        self.first_name_input.blockSignals(True)
        self.last_name_input.blockSignals(True)
        self.position_input.blockSignals(True)
        self.captaincy_dropdown.blockSignals(True)
        self.playing_time_dropdown.blockSignals(True)
        self.contract_dropdown.blockSignals(True)
        self.foreign_checkbox.blockSignals(True)
        self.youth_checkbox.blockSignals(True)
        self.injury_checkbox.blockSignals(True)

        # Update UI fields
        self.first_name_input.setText(attributes.get("first_name", ""))
        self.last_name_input.setText(attributes.get("last_name", ""))
        self.position_input.setText(attributes.get("position", ""))
        self.captaincy_dropdown.setCurrentText(
            attributes.get("captaincy", "None"))
        self.playing_time_dropdown.setCurrentText(
            attributes.get("playing_time", "None"))
        self.contract_dropdown.setCurrentText(
            attributes.get("contract", "None"))
        self.foreign_checkbox.setChecked(attributes.get("foreign", False))
        self.youth_checkbox.setChecked(attributes.get("youth", False))
        self.injury_checkbox.setChecked(attributes.get("injury", False))

        # Unblock signals after setting values
        self.first_name_input.blockSignals(False)
        self.last_name_input.blockSignals(False)
        self.position_input.blockSignals(False)
        self.captaincy_dropdown.blockSignals(False)
        self.playing_time_dropdown.blockSignals(False)
        self.contract_dropdown.blockSignals(False)
        self.foreign_checkbox.blockSignals(False)
        self.youth_checkbox.blockSignals(False)
        self.injury_checkbox.blockSignals(False)

        print(attributes)

    def update_selected_player(self):
        # Updates the selected player's attributes and UI.
        if not self.selected_player:
            return

        # Update attributes from customizationContainer
        updated_attributes = {
            "first_name": self.first_name_input.text(),
            "last_name": self.last_name_input.text(),
            "position": self.position_input.text(),
            "captaincy": self.captaincy_dropdown.currentText(),
            "playing_time": self.playing_time_dropdown.currentText(),
            "contract": self.contract_dropdown.currentText(),
            "foreign": self.foreign_checkbox.isChecked(),
            "youth": self.youth_checkbox.isChecked(),
            "injury": self.injury_checkbox.isChecked()
        }

        if updated_attributes != self.selected_player.attributes:
            self.selected_player.attributes.update(updated_attributes)
            self.selected_player.update_ui()
            self.save_players()

    def add_player(self, attributes=None):
        if attributes is None:
            attributes = {
                "first_name": "First",
                "last_name": "Last",
                "position": "Pos",
                "captaincy": "None",
                "playing_time": "None",
                "contract": "None",
                "foreign": False,
                "youth": False,
                "injury": False,
                "loan": "",
                "transfer": ""
            }

        new_player_container = PlayerContainer(
            self.player_list, attributes, self)
        self.player_list_layout.addWidget(new_player_container)

    def load_saved_players(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.main_window, "Open Player Sheet", "", "JSON Files (*.json)")

        if file_path:
            saved_players = StorageManager.load_players(file_path)
            self.clear_players()
            for player in saved_players:
                self.add_player(player)

    def save_players(self):
        players = [
            self.player_list_layout.itemAt(
                i).widget().player_item.get_player_data()
            for i in range(self.player_list_layout.count())
        ]

        StorageManager.save_players(players)

    def clear_players(self):
        while self.player_list_layout.count():
            widget = self.player_list_layout.takeAt(0).widget()
            if widget():
                widget.deleteLater()
