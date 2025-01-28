from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

# Define playing time colors
PLAYING_TIME_COLORS = {
    "Star": "yellow",
    "Important": "orange",
    "Starter": "lightgreen",
    "Squad Player": "green",
    "Rotation": "blue",
    "Fringe": "brown",
    "Emergency Backup": "gray",
    "Youngster": "black"
}

# Define contract icons
CONTRACT_ICONS = {
    "Offered": "assets/icons/contract_offered.png",
    "Expiring": "assets/icons/contract_expiring.png",
    "Set for Release": "assets/icons/contract_release.png"
}

# Define captaincy icons
CAPTAINCY_ICONS = {
    "Captain": "assets/icons/captain.png",
    "Vice Captain": "assets/icons/vice_captain.png"
}

# Define attribute images for checkboxes
ATTRIBUTE_ICONS = {
    "foreign": "assets/icons/foreign.png",
    "youth": "assets/icons/youth.png",
    "injury": "assets/icons/injury.png"
}


class AttributeManager:
    @staticmethod
    def apply_attributes(player_card, attributes):
        """
        Apply attribute visuals to a player card.

        :param player_card: The PlayerItem widget
        :param attributes: A dictionary containing player attributes
        """

        # Apply playing time color to top border
        playing_time = attributes.get("playing_time", None)
        if playing_time and playing_time in PLAYING_TIME_COLORS:
            color = PLAYING_TIME_COLORS[playing_time]
            new_style = f"""
                QFrame#horizontalFrame {{
                    border-top: 10px solid {color};
                }}
            """
            player_card.setStyleSheet(new_style)

        # Apply contract icon (left side)
        contract = attributes.get("contract", None)
        if contract and contract in CONTRACT_ICONS:
            contract_label = QLabel(player_card)
            contract_label.setGeometry(5, 50, 17, 17)
            contract_label.setPixmap(
                QPixmap(CONTRACT_ICONS[contract]))
            contract_label.setStyleSheet(f"""
                QFrame {{
                    background-color: red;
                    border-radius: 30px;
                }}
            """)

        # Apply captaincy icon (top-center)
        captaincy = attributes.get("captaincy", None)
        if captaincy and captaincy in CAPTAINCY_ICONS:
            captaincy_label = QLabel(player_card)
            captaincy_label.setGeometry(60, 2, 150, 25)
            captaincy_label.setScaledContents(True)
            captaincy_label.setPixmap(
                QPixmap(CAPTAINCY_ICONS[captaincy]))

        # Apply icons for foreign, youth, injury (right side)
        icon_x = 250  # Right alignment
        icon_y = 10  # Start from the top

        for attr, icon_path in ATTRIBUTE_ICONS.items():
            if attributes.get(attr, False):  # If attribute is True
                attr_label = QLabel(player_card)
                attr_label.setPixmap(QPixmap(icon_path).scaled(20, 20))
                attr_label.move(icon_x, icon_y)
                icon_y += 25  # Stack them vertically
