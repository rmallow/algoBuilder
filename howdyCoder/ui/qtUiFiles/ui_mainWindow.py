# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

from ..controlWidget import ControlWidget
from ..create.createWidget import CreateWidget
from ..globalParameterPage import GlobalParameterPage
from ..mainOutputView import mainOutputView
from . import res_rc

class Ui_HowdyCoder(object):
    def setupUi(self, HowdyCoder):
        if not HowdyCoder.objectName():
            HowdyCoder.setObjectName(u"HowdyCoder")
        HowdyCoder.resize(1104, 714)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HowdyCoder.sizePolicy().hasHeightForWidth())
        HowdyCoder.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/app-icons/1024.png", QSize(), QIcon.Normal, QIcon.Off)
        HowdyCoder.setWindowIcon(icon)
        HowdyCoder.setStyleSheet(u"")
        self.actionStatus = QAction(HowdyCoder)
        self.actionStatus.setObjectName(u"actionStatus")
        self.actionStatus.setMenuRole(QAction.NoRole)
        self.actionLoad_Config = QAction(HowdyCoder)
        self.actionLoad_Config.setObjectName(u"actionLoad_Config")
        self.actionLoad_Config.setMenuRole(QAction.NoRole)
        self.actionLogging = QAction(HowdyCoder)
        self.actionLogging.setObjectName(u"actionLogging")
        self.actionLogging.setMenuRole(QAction.NoRole)
        self.action_help_menu = QAction(HowdyCoder)
        self.action_help_menu.setObjectName(u"action_help_menu")
        icon1 = QIcon()
        icon1.addFile(u":/images/help.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/help.png", QSize(), QIcon.Normal, QIcon.On)
        self.action_help_menu.setIcon(icon1)
        self.action_help_menu.setMenuRole(QAction.TextHeuristicRole)
        self.invisible_action = QAction(HowdyCoder)
        self.invisible_action.setObjectName(u"invisible_action")
        self.invisible_action.setMenuRole(QAction.NoRole)
        self.action_tutorial = QAction(HowdyCoder)
        self.action_tutorial.setObjectName(u"action_tutorial")
        self.action_tutorial.setMenuRole(QAction.NoRole)
        self.action_documentation = QAction(HowdyCoder)
        self.action_documentation.setObjectName(u"action_documentation")
        self.action_documentation.setMenuRole(QAction.NoRole)
        self.action_parameter_and_key = QAction(HowdyCoder)
        self.action_parameter_and_key.setObjectName(u"action_parameter_and_key")
        self.action_parameter_and_key.setMenuRole(QAction.NoRole)
        self.action_output = QAction(HowdyCoder)
        self.action_output.setObjectName(u"action_output")
        self.action_output.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(HowdyCoder)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.return_to_dashboard_button = QPushButton(self.centralwidget)
        self.return_to_dashboard_button.setObjectName(u"return_to_dashboard_button")

        self.verticalLayout.addWidget(self.return_to_dashboard_button)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 4)
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(6)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.controlPage = ControlWidget()
        self.controlPage.setObjectName(u"controlPage")
        self.stackedWidget.addWidget(self.controlPage)
        self.global_parameter_page = GlobalParameterPage()
        self.global_parameter_page.setObjectName(u"global_parameter_page")
        self.stackedWidget.addWidget(self.global_parameter_page)
        self.createPage = CreateWidget()
        self.createPage.setObjectName(u"createPage")
        self.stackedWidget.addWidget(self.createPage)
        self.outputPage = mainOutputView()
        self.outputPage.setObjectName(u"outputPage")
        self.stackedWidget.addWidget(self.outputPage)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget)

        HowdyCoder.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(HowdyCoder)
        self.statusbar.setObjectName(u"statusbar")
        HowdyCoder.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(HowdyCoder)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(32, 40))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(False)
        HowdyCoder.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_output)
        self.toolBar.addAction(self.actionStatus)
        self.toolBar.addAction(self.actionLoad_Config)
        self.toolBar.addAction(self.actionLogging)
        self.toolBar.addAction(self.action_parameter_and_key)
        self.toolBar.addAction(self.invisible_action)
        self.toolBar.addAction(self.action_help_menu)

        self.retranslateUi(HowdyCoder)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(HowdyCoder)
    # setupUi

    def retranslateUi(self, HowdyCoder):
        HowdyCoder.setWindowTitle(QCoreApplication.translate("HowdyCoder", u"Howdy Coder", None))
        self.actionStatus.setText(QCoreApplication.translate("HowdyCoder", u"Status", None))
        self.actionLoad_Config.setText(QCoreApplication.translate("HowdyCoder", u"Load Config", None))
        self.actionLogging.setText(QCoreApplication.translate("HowdyCoder", u"Logging", None))
        self.action_help_menu.setText(QCoreApplication.translate("HowdyCoder", u"Help", None))
#if QT_CONFIG(tooltip)
        self.action_help_menu.setToolTip(QCoreApplication.translate("HowdyCoder", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.invisible_action.setText("")
        self.action_tutorial.setText(QCoreApplication.translate("HowdyCoder", u"Tutorial", None))
        self.action_documentation.setText(QCoreApplication.translate("HowdyCoder", u"Documentation", None))
        self.action_parameter_and_key.setText(QCoreApplication.translate("HowdyCoder", u"Parameters and Keys", None))
        self.action_parameter_and_key.setIconText(QCoreApplication.translate("HowdyCoder", u"Parameters and Keys", None))
#if QT_CONFIG(tooltip)
        self.action_parameter_and_key.setToolTip(QCoreApplication.translate("HowdyCoder", u"Parameters and Keys", None))
#endif // QT_CONFIG(tooltip)
        self.action_output.setText(QCoreApplication.translate("HowdyCoder", u"View Output", None))
        self.return_to_dashboard_button.setText(QCoreApplication.translate("HowdyCoder", u"Return to Dashboard", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("HowdyCoder", u"toolBar", None))
    # retranslateUi

