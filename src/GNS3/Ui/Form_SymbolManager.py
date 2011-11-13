# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_SymbolManager.ui'
#
# Created: Sat Nov 12 17:09:56 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SymbolManager(object):
    def setupUi(self, SymbolManager):
        SymbolManager.setObjectName(_fromUtf8("SymbolManager"))
        SymbolManager.resize(703, 575)
        SymbolManager.setWindowTitle(QtGui.QApplication.translate("SymbolManager", "Symbol Manager", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addFile(_fromUtf8(":/images/logo_icon.png"))
        SymbolManager.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(SymbolManager)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.groupBox_2 = QtGui.QGroupBox(SymbolManager)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SymbolManager", "Symbol librairies", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setText(QtGui.QApplication.translate("SymbolManager", "Library path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout1.addWidget(self.label_3, 0, 0, 1, 4)
        self.lineEditLibrary = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditLibrary.setObjectName(_fromUtf8("lineEditLibrary"))
        self.gridlayout1.addWidget(self.lineEditLibrary, 1, 0, 1, 3)
        self.toolButtonLibrary = QtGui.QToolButton(self.groupBox_2)
        self.toolButtonLibrary.setText(QtGui.QApplication.translate("SymbolManager", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonLibrary.setObjectName(_fromUtf8("toolButtonLibrary"))
        self.gridlayout1.addWidget(self.toolButtonLibrary, 1, 3, 1, 1)
        self.pushButtonAddLibrary = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonAddLibrary.setText(QtGui.QApplication.translate("SymbolManager", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddLibrary.setObjectName(_fromUtf8("pushButtonAddLibrary"))
        self.gridlayout1.addWidget(self.pushButtonAddLibrary, 2, 0, 1, 1)
        self.pushButtonRemoveLibrary = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonRemoveLibrary.setText(QtGui.QApplication.translate("SymbolManager", "&Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemoveLibrary.setObjectName(_fromUtf8("pushButtonRemoveLibrary"))
        self.gridlayout1.addWidget(self.pushButtonRemoveLibrary, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(16, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem, 2, 2, 1, 2)
        self.gridlayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        spacerItem1 = QtGui.QSpacerItem(75, 161, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.pushButtonAdd = QtGui.QPushButton(SymbolManager)
        self.pushButtonAdd.setText(QtGui.QApplication.translate("SymbolManager", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.vboxlayout.addWidget(self.pushButtonAdd)
        self.pushButtonRemove = QtGui.QPushButton(SymbolManager)
        self.pushButtonRemove.setText(QtGui.QApplication.translate("SymbolManager", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemove.setObjectName(_fromUtf8("pushButtonRemove"))
        self.vboxlayout.addWidget(self.pushButtonRemove)
        spacerItem2 = QtGui.QSpacerItem(75, 133, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)
        self.gridlayout.addLayout(self.vboxlayout, 0, 1, 2, 1)
        self.groupBox = QtGui.QGroupBox(SymbolManager)
        self.groupBox.setTitle(QtGui.QApplication.translate("SymbolManager", "Customized node settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout2 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("SymbolManager", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEditNodeName = QtGui.QLineEdit(self.groupBox)
        self.lineEditNodeName.setObjectName(_fromUtf8("lineEditNodeName"))
        self.gridlayout2.addWidget(self.lineEditNodeName, 0, 1, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("SymbolManager", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout2.addWidget(self.label, 1, 0, 1, 1)
        self.comboBoxNodeType = QtGui.QComboBox(self.groupBox)
        self.comboBoxNodeType.setObjectName(_fromUtf8("comboBoxNodeType"))
        self.gridlayout2.addWidget(self.comboBoxNodeType, 1, 1, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(141, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem3, 2, 0, 1, 2)
        self.pushButtonApply = QtGui.QPushButton(self.groupBox)
        self.pushButtonApply.setText(QtGui.QApplication.translate("SymbolManager", "&Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonApply.setObjectName(_fromUtf8("pushButtonApply"))
        self.gridlayout2.addWidget(self.pushButtonApply, 2, 2, 1, 1)
        self.gridlayout.addWidget(self.groupBox, 0, 2, 1, 1)
        self.treeWidgetSymbols = QtGui.QTreeWidget(SymbolManager)
        self.treeWidgetSymbols.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidgetSymbols.setIconSize(QtCore.QSize(24, 24))
        self.treeWidgetSymbols.setObjectName(_fromUtf8("treeWidgetSymbols"))
        self.treeWidgetSymbols.headerItem().setText(0, QtGui.QApplication.translate("SymbolManager", "Available symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.gridlayout.addWidget(self.treeWidgetSymbols, 1, 0, 1, 1)
        self.treeWidgetNodes = QtGui.QTreeWidget(SymbolManager)
        self.treeWidgetNodes.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidgetNodes.setIconSize(QtCore.QSize(24, 24))
        self.treeWidgetNodes.setRootIsDecorated(False)
        self.treeWidgetNodes.setObjectName(_fromUtf8("treeWidgetNodes"))
        self.treeWidgetNodes.headerItem().setText(0, QtGui.QApplication.translate("SymbolManager", "Customized nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.gridlayout.addWidget(self.treeWidgetNodes, 1, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SymbolManager)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 3)

        self.retranslateUi(SymbolManager)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SymbolManager.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SymbolManager.reject)
        QtCore.QMetaObject.connectSlotsByName(SymbolManager)
        SymbolManager.setTabOrder(self.lineEditLibrary, self.toolButtonLibrary)
        SymbolManager.setTabOrder(self.toolButtonLibrary, self.pushButtonAddLibrary)
        SymbolManager.setTabOrder(self.pushButtonAddLibrary, self.pushButtonRemoveLibrary)
        SymbolManager.setTabOrder(self.pushButtonRemoveLibrary, self.treeWidgetSymbols)
        SymbolManager.setTabOrder(self.treeWidgetSymbols, self.pushButtonAdd)
        SymbolManager.setTabOrder(self.pushButtonAdd, self.pushButtonRemove)
        SymbolManager.setTabOrder(self.pushButtonRemove, self.lineEditNodeName)
        SymbolManager.setTabOrder(self.lineEditNodeName, self.comboBoxNodeType)
        SymbolManager.setTabOrder(self.comboBoxNodeType, self.pushButtonApply)
        SymbolManager.setTabOrder(self.pushButtonApply, self.treeWidgetNodes)
        SymbolManager.setTabOrder(self.treeWidgetNodes, self.buttonBox)

    def retranslateUi(self, SymbolManager):
        pass

import svg_resources_rc
