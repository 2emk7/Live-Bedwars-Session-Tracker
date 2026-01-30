# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BWSphereSettingsPage.ui'
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
    QSizePolicy, QWidget)

class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        if not SettingsPage.objectName():
            SettingsPage.setObjectName(u"SettingsPage")
        SettingsPage.resize(400, 300)
        icon = QIcon(QIcon.fromTheme(u"dialog-warning"))
        SettingsPage.setWindowIcon(icon)
        self.SettingsHeader = QLabel(SettingsPage)
        self.SettingsHeader.setObjectName(u"SettingsHeader")
        self.SettingsHeader.setGeometry(QRect(80, 10, 265, 16))
        self.lineEdit = QLineEdit(SettingsPage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(9, 68, 381, 21))
        self.latestlogHeader = QLabel(SettingsPage)
        self.latestlogHeader.setObjectName(u"latestlogHeader")
        self.latestlogHeader.setEnabled(True)
        self.latestlogHeader.setGeometry(QRect(4, 40, 391, 61))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.latestlogHeader.setFont(font)
        self.latestlogHeader.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.latestlogHeader.setAutoFillBackground(False)
        self.latestlogHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.latestlogHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.latestlogHeader.setLineWidth(2)
        self.latestlogHeader.setMidLineWidth(0)
        self.latestlogHeader.setScaledContents(False)
        self.latestlogHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.latestlogHeader.setWordWrap(True)
        self.SettingsHeader.raise_()
        self.latestlogHeader.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(SettingsPage)

        QMetaObject.connectSlotsByName(SettingsPage)
    # setupUi

    def retranslateUi(self, SettingsPage):
        SettingsPage.setWindowTitle(QCoreApplication.translate("SettingsPage", u"Settings", None))
        self.SettingsHeader.setText(QCoreApplication.translate("SettingsPage", u"============ Settings ============", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("SettingsPage", u"Enter latest.log PATH", None))
        self.latestlogHeader.setText(QCoreApplication.translate("SettingsPage", u"latest.log file location:", None))
    # retranslateUi

