from ...core.dataStructs import AlgoSettings
from .createBasePage import CreateBasePage

from ..uiConstants import PageKeys
from ..qtUiFiles import ui_createDataSourceAdd

from ...core.commonGlobals import DATA_SOURCES, ACTION_LIST
import typing

from PySide6 import QtWidgets, QtCore, QtGui

ACTION_TOP_TEXT = "Actions act on data either from data sources and/or events. There are two types of actions, events which take input data and apply a function to output data, and triggers which take input data and determine if a criteria is met to trigger an output function. "

NAME_ROLE = QtCore.Qt.ItemDataRole.UserRole + 1


class CreateAddPageBase(CreateBasePage):
    """

    DEPRECATED
    DEPRECATED
    DEPRECATED
    DEPRECATED
    DEPRECATED
    DEPRECATED
    DEPRECATED

    """

    TUTORIAL_RESOURCE_PREFIX = "CreateAdd"

    def __init__(
        self,
        current_config: AlgoSettings,
        skip_page: PageKeys,
        top_text="",
        parent: typing.Optional[QtWidgets.QWidget] = None,
    ):
        super().__init__(current_config, self.TUTORIAL_RESOURCE_PREFIX, parent=parent)

        self._ui = ui_createDataSourceAdd.Ui_CreateDataSourceAdd()
        self._ui.setupUi(self)
        if top_text:
            self._ui.topText.setText(top_text)
        self._dataSourcesModel = QtGui.QStandardItemModel()
        self._ui.dataSourcesView.setModel(self._dataSourcesModel)
        self._skip_page: PageKeys = skip_page
        self._ui.addButton.released.connect(self.nextPage)
        self._ui.skipButton.released.connect(
            lambda: self.manualExit.emit(self._skip_page)
        )
        self._ui.editButton.released.connect(self.editConfig)
        self._ui.removeButton.released.connect(self.removeSelected)
        self.next_enabled = False

    def save(self) -> None:
        pass

    def reset(self) -> None:
        self._ui.skipButton.setEnabled(False)
        self._dataSourcesModel.clear()
        self.getConfig().clear()
        return super().reset()

    def setGroupModel(self):
        self._dataSourcesModel.clear()
        for k, v in self.getConfigGroup().items():
            item = QtGui.QStandardItem(f"{k} : {v.type_}")
            item.setData(k, NAME_ROLE)
            self._dataSourcesModel.appendRow(item)
        self._ui.skipButton.setEnabled(len(self.getConfigGroup()) != 0)

    def loadPage(self):
        super().loadPage()
        self.getConfig().clear()
        self.setGroupModel()

    def getCurrentSelectionName(self):
        name = ""
        selection = self._ui.dataSourcesView.selectionModel().selectedIndexes()
        if len(selection) == 1:
            name = selection[0].data(NAME_ROLE)
        return name

    def removeSelected(self):
        if curr := self.getCurrentSelectionName():
            del self.getConfigGroup()[curr]
            self.setGroupModel()

    def getTutorialClasses(self) -> typing.List:
        return [self]

    def editConfig(self):
        if curr := self.getCurrentSelectionName():
            self.getConfig().clear()
            self.getConfig().inPlaceCopy(self.getConfigGroup()[curr])
            self.nextPage.emit()


class CreateDataSourceAddPage(CreateAddPageBase):
    PAGE_KEY = PageKeys.ADD_DATA_SOURCE

    def __init__(
        self,
        current_config: AlgoSettings,
        parent: typing.Optional[QtWidgets.QWidget] = None,
    ):
        super().__init__(current_config, PageKeys.ADD_ACTION, parent=parent)


class CreateActionAddPage(CreateAddPageBase):
    PAGE_KEY = PageKeys.ADD_ACTION

    def __init__(
        self,
        current_config: AlgoSettings,
        parent: typing.Optional[QtWidgets.QWidget] = None,
    ):
        super().__init__(
            current_config,
            PageKeys.FINAL_CONFIRM,
            top_text=ACTION_TOP_TEXT,
            parent=parent,
        )
        self.back_enabled = False
