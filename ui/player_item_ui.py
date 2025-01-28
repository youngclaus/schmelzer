# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\1.Projects\sabitzer\ui\player_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_playerItem(object):
    def setupUi(self, playerItem):
        playerItem.setObjectName("playerItem")
        playerItem.setWindowModality(QtCore.Qt.NonModal)
        playerItem.resize(250, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(playerItem.sizePolicy().hasHeightForWidth())
        playerItem.setSizePolicy(sizePolicy)
        playerItem.setMinimumSize(QtCore.QSize(0, 0))
        playerItem.setMaximumSize(QtCore.QSize(250, 75))
        playerItem.setLayoutDirection(QtCore.Qt.LeftToRight)
        playerItem.setAutoFillBackground(True)
        playerItem.setStyleSheet("")
        self.horizontalFrame = QtWidgets.QFrame(playerItem)
        self.horizontalFrame.setGeometry(QtCore.QRect(0, 0, 250, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(250, 75))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(250, 75))
        self.horizontalFrame.setAutoFillBackground(False)
        self.horizontalFrame.setStyleSheet("")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.positionBox = QtWidgets.QLabel(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.positionBox.sizePolicy().hasHeightForWidth())
        self.positionBox.setSizePolicy(sizePolicy)
        self.positionBox.setMinimumSize(QtCore.QSize(80, 0))
        self.positionBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.positionBox.setText("")
        self.positionBox.setAlignment(QtCore.Qt.AlignCenter)
        self.positionBox.setObjectName("positionBox")
        self.horizontalLayout.addWidget(self.positionBox)
        self.verticalWidget = QtWidgets.QWidget(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setAutoFillBackground(False)
        self.verticalWidget.setStyleSheet("")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.firstNameBox = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstNameBox.sizePolicy().hasHeightForWidth())
        self.firstNameBox.setSizePolicy(sizePolicy)
        self.firstNameBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.firstNameBox.setText("")
        self.firstNameBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.firstNameBox.setObjectName("firstNameBox")
        self.verticalLayout_2.addWidget(self.firstNameBox)
        self.lastNameBox = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastNameBox.sizePolicy().hasHeightForWidth())
        self.lastNameBox.setSizePolicy(sizePolicy)
        self.lastNameBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lastNameBox.setText("")
        self.lastNameBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lastNameBox.setObjectName("lastNameBox")
        self.verticalLayout_2.addWidget(self.lastNameBox)
        self.horizontalLayout.addWidget(self.verticalWidget)
        self.horizontalLayout.setStretch(1, 5)

        self.retranslateUi(playerItem)
        QtCore.QMetaObject.connectSlotsByName(playerItem)

    def retranslateUi(self, playerItem):
        _translate = QtCore.QCoreApplication.translate
        playerItem.setWindowTitle(_translate("playerItem", "Form"))
