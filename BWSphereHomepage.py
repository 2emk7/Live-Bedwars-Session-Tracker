# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BWSphereHomepage.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(400, 300)
        icon = QIcon(QIcon.fromTheme(u"dialog-warning"))
        HomePage.setWindowIcon(icon)
        HomePage.setWindowOpacity(1.000000000000000)
        HomePage.setAutoFillBackground(False)
        self.Header = QLabel(HomePage)
        self.Header.setObjectName(u"Header")
        self.Header.setGeometry(QRect(70, 10, 265, 16))
        self.layoutWidget = QWidget(HomePage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 40, 61, 241))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.WINS_Label_2 = QLabel(self.layoutWidget)
        self.WINS_Label_2.setObjectName(u"WINS_Label_2")
        self.WINS_Label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.WINS_Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.LOSSES_Label_2 = QLabel(self.layoutWidget)
        self.LOSSES_Label_2.setObjectName(u"LOSSES_Label_2")

        self.verticalLayout_2.addWidget(self.LOSSES_Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.BD__Label_2 = QLabel(self.layoutWidget)
        self.BD__Label_2.setObjectName(u"BD__Label_2")

        self.verticalLayout_2.addWidget(self.BD__Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.BL__Label_2 = QLabel(self.layoutWidget)
        self.BL__Label_2.setObjectName(u"BL__Label_2")

        self.verticalLayout_2.addWidget(self.BL__Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.FK__Label_2 = QLabel(self.layoutWidget)
        self.FK__Label_2.setObjectName(u"FK__Label_2")

        self.verticalLayout_2.addWidget(self.FK__Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.FD__Label_2 = QLabel(self.layoutWidget)
        self.FD__Label_2.setObjectName(u"FD__Label_2")

        self.verticalLayout_2.addWidget(self.FD__Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.BBLR__Label_2 = QLabel(self.layoutWidget)
        self.BBLR__Label_2.setObjectName(u"BBLR__Label_2")

        self.verticalLayout_2.addWidget(self.BBLR__Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.FKDR__Label_2 = QLabel(self.layoutWidget)
        self.FKDR__Label_2.setObjectName(u"FKDR__Label_2")

        self.verticalLayout_2.addWidget(self.FKDR__Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.WLR_Label_2 = QLabel(self.layoutWidget)
        self.WLR_Label_2.setObjectName(u"WLR_Label_2")

        self.verticalLayout_2.addWidget(self.WLR_Label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Alert_Label = QLabel(HomePage)
        self.Alert_Label.setObjectName(u"Alert_Label")
        self.Alert_Label.setEnabled(True)
        self.Alert_Label.setGeometry(QRect(200, 90, 161, 81))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.Alert_Label.setFont(font)
        self.Alert_Label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Alert_Label.setAutoFillBackground(False)
        self.Alert_Label.setFrameShape(QFrame.Shape.StyledPanel)
        self.Alert_Label.setFrameShadow(QFrame.Shadow.Raised)
        self.Alert_Label.setLineWidth(2)
        self.Alert_Label.setMidLineWidth(0)
        self.Alert_Label.setScaledContents(False)
        self.Alert_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Alert_Label.setWordWrap(True)
        self.EnterNameBox = QLineEdit(HomePage)
        self.EnterNameBox.setObjectName(u"EnterNameBox")
        self.EnterNameBox.setGeometry(QRect(220, 263, 120, 21))
        font1 = QFont()
        font1.setKerning(True)
        self.EnterNameBox.setFont(font1)
        self.EnterNameBox.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.EnterNameBox.setAutoFillBackground(False)
        self.EnterNameBox.setMaxLength(16)
        self.EnterNameBox.setFrame(False)
        self.EnterNameBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TrackingForWhoBox = QLabel(HomePage)
        self.TrackingForWhoBox.setObjectName(u"TrackingForWhoBox")
        self.TrackingForWhoBox.setEnabled(True)
        self.TrackingForWhoBox.setGeometry(QRect(210, 242, 140, 50))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.TrackingForWhoBox.setFont(font2)
        self.TrackingForWhoBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TrackingForWhoBox.setAutoFillBackground(False)
        self.TrackingForWhoBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.TrackingForWhoBox.setFrameShadow(QFrame.Shadow.Raised)
        self.TrackingForWhoBox.setLineWidth(2)
        self.TrackingForWhoBox.setMidLineWidth(0)
        self.TrackingForWhoBox.setScaledContents(False)
        self.TrackingForWhoBox.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.TrackingForWhoBox.setWordWrap(True)
        self.ResetButton = QPushButton(HomePage)
        self.ResetButton.setObjectName(u"ResetButton")
        self.ResetButton.setGeometry(QRect(351, 275, 51, 26))
        self.ResetButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(81, 81, 81);\n"
"}")
        self.layoutWidget1 = QWidget(HomePage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 40, 80, 241))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.WINS_Label = QLabel(self.layoutWidget1)
        self.WINS_Label.setObjectName(u"WINS_Label")
        self.WINS_Label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.WINS_Label, 0, Qt.AlignmentFlag.AlignRight)

        self.LOSSES_Label = QLabel(self.layoutWidget1)
        self.LOSSES_Label.setObjectName(u"LOSSES_Label")

        self.verticalLayout.addWidget(self.LOSSES_Label, 0, Qt.AlignmentFlag.AlignRight)

        self.BD__Label = QLabel(self.layoutWidget1)
        self.BD__Label.setObjectName(u"BD__Label")

        self.verticalLayout.addWidget(self.BD__Label, 0, Qt.AlignmentFlag.AlignRight)

        self.BL__Label = QLabel(self.layoutWidget1)
        self.BL__Label.setObjectName(u"BL__Label")

        self.verticalLayout.addWidget(self.BL__Label, 0, Qt.AlignmentFlag.AlignRight)

        self.FK__Label = QLabel(self.layoutWidget1)
        self.FK__Label.setObjectName(u"FK__Label")

        self.verticalLayout.addWidget(self.FK__Label, 0, Qt.AlignmentFlag.AlignRight)

        self.FD__Label = QLabel(self.layoutWidget1)
        self.FD__Label.setObjectName(u"FD__Label")

        self.verticalLayout.addWidget(self.FD__Label, 0, Qt.AlignmentFlag.AlignRight)

        self.BBLR__Label = QLabel(self.layoutWidget1)
        self.BBLR__Label.setObjectName(u"BBLR__Label")

        self.verticalLayout.addWidget(self.BBLR__Label, 0, Qt.AlignmentFlag.AlignRight)

        self.FKDR__Label = QLabel(self.layoutWidget1)
        self.FKDR__Label.setObjectName(u"FKDR__Label")

        self.verticalLayout.addWidget(self.FKDR__Label, 0, Qt.AlignmentFlag.AlignRight)

        self.WLR_Label = QLabel(self.layoutWidget1)
        self.WLR_Label.setObjectName(u"WLR_Label")

        self.verticalLayout.addWidget(self.WLR_Label, 0, Qt.AlignmentFlag.AlignRight)

        self.settingsButton = QToolButton(HomePage)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(368, 4, 31, 31))
        self.settingsButton.setMouseTracking(False)
        self.settingsButton.setStyleSheet(u"QToolButton:hover{\n"
"	background-color: rgb(81, 81, 81);\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.settingsButton.setIcon(icon1)
        self.settingsButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.layoutWidget1.raise_()
        self.TrackingForWhoBox.raise_()
        self.Header.raise_()
        self.layoutWidget1.raise_()
        self.Alert_Label.raise_()
        self.EnterNameBox.raise_()
        self.ResetButton.raise_()
        self.settingsButton.raise_()

        self.retranslateUi(HomePage)

        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"BWSphere", None))
        self.Header.setText(QCoreApplication.translate("HomePage", u"============Session Stats============", None))
        self.WINS_Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.LOSSES_Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.BD__Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.BL__Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.FK__Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.FD__Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.BBLR__Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.FKDR__Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.WLR_Label_2.setText(QCoreApplication.translate("HomePage", u"0", None))
        self.Alert_Label.setText(QCoreApplication.translate("HomePage", u"Tracking will not start until a username is entered", None))
        self.EnterNameBox.setText("")
        self.EnterNameBox.setPlaceholderText(QCoreApplication.translate("HomePage", u"Enter Username", None))
        self.TrackingForWhoBox.setText(QCoreApplication.translate("HomePage", u"Tracking for:", None))
        self.ResetButton.setText(QCoreApplication.translate("HomePage", u"Reset", None))
        self.WINS_Label.setText(QCoreApplication.translate("HomePage", u"WINS", None))
        self.LOSSES_Label.setText(QCoreApplication.translate("HomePage", u"LOSSES", None))
        self.BD__Label.setText(QCoreApplication.translate("HomePage", u"BEDS BROKE", None))
        self.BL__Label.setText(QCoreApplication.translate("HomePage", u"BEDS LOST", None))
        self.FK__Label.setText(QCoreApplication.translate("HomePage", u"FINAL KILLS", None))
        self.FD__Label.setText(QCoreApplication.translate("HomePage", u"FINAL DEATHS", None))
        self.BBLR__Label.setText(QCoreApplication.translate("HomePage", u"BBLR", None))
        self.FKDR__Label.setText(QCoreApplication.translate("HomePage", u"FKDR", None))
        self.WLR_Label.setText(QCoreApplication.translate("HomePage", u"WLR", None))
        self.settingsButton.setText("")
    # retranslateUi

