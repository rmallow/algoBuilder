import typing
from .outputSelect import outputSelect
from .outputViewFeed import OutputViewFeed
from .outputViewGraph import outputViewGraph
from .outputViewPrinted import OutputViewPrinted
from .uiConstants import outputTypesEnum
from .mainOutputViewModel import mainOutputViewModel
from .tutorialOverlay import AbstractTutorialClass

from .util import animations, abstractQt

from ..core.commonGlobals import TYPE, ITEM
from ..commonUtil import mpLogging

import typing

from PySide6 import QtWidgets, QtCore

OUTPUT_VIEW_TYPE_TO_VIEW_CLASS = {
    outputTypesEnum.TABLE.value: OutputViewFeed,
    outputTypesEnum.GRAPH.value: outputViewGraph,
    outputTypesEnum.PRINTED.value: OutputViewPrinted,
}


# this class is used in a generated file
class mainOutputView(
    AbstractTutorialClass,
    QtWidgets.QWidget,
    metaclass=abstractQt.getAbstractQtResolver(
        QtWidgets.QWidget, AbstractTutorialClass
    ),
):
    TUTORIAL_RESOURCE_PREFIX = "MainOutputView"

    def __new__(self, *args, **kwargs):
        abstractQt.handleAbstractMethods(self)
        return super().__new__(self, *args, **kwargs)

    def __init__(self, parent=None):
        super().__init__(self.TUTORIAL_RESOURCE_PREFIX, parent)
        self.mainOutputViewModel: mainOutputViewModel = mainOutputViewModel(self)

        """
        Set up the UI, no UI file to load but it will be:
        layout
            selector
            main window
                dock widgets
        """
        self._title_set = set()
        self._outer_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self._outer_layout)
        self._outer_layout.setSpacing(0)

        self._current_selector = outputSelect(self.mainOutputViewModel)
        self._current_selector.selectionFinished.connect(self.onSelectionFinished)
        self._outer_layout.addWidget(self._current_selector)

        self._sub_main_window = QtWidgets.QMainWindow()
        w = QtWidgets.QWidget(self._sub_main_window)
        w.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self._sub_main_window.setCentralWidget(w)
        self._sub_main_window.setDockNestingEnabled(True)
        self._outer_layout.addWidget(self._sub_main_window)

    @QtCore.Slot()
    def onSelectionFinished(self, selection_settings):
        """
        Output select is finished, send settings to mainOutputViewModel to translate to message
        """
        oView, model = None, self.mainOutputViewModel.setupOutputView(
            selection_settings
        )
        x = 1
        title = f"{selection_settings[ITEM]} - {selection_settings[TYPE]}{x}"
        while title in self._title_set:
            x += 1
            title = f"{selection_settings[ITEM]} - {selection_settings[TYPE]}{x}"
        self._title_set.add(title)
        dock = QtWidgets.QDockWidget(title, self._sub_main_window)
        oView = OUTPUT_VIEW_TYPE_TO_VIEW_CLASS[selection_settings[TYPE]](
            model, selection_settings, dock
        )

        self._current_selector = outputSelect(self.mainOutputViewModel, self)
        self._current_selector.selectionFinished.connect(self.onSelectionFinished)

        animations.fadeStart(
            self, self.sender(), self._current_selector, self._outer_layout
        )

        if oView is not None:
            dock.setWidget(oView)
            self._sub_main_window.addDockWidget(
                QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, dock
            )
        else:
            mpLogging.error("Output View was supposed to be made but was not")

    def getTutorialClasses(self) -> typing.List:
        res = [self] + self._current_selector.getTutorialClasses()
        for view_type in [outputViewGraph, OutputViewFeed]:
            if find_res := self._sub_main_window.findChild(view_type):
                res.extend(find_res.getTutorialClasses())
        return res

    def loadMainPage(self):
        pass

    def leaveMainPage(self):
        pass
