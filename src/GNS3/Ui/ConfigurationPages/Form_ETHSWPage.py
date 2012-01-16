# vim: expandtab ts=4 sw=4 sts=4:
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_ETHSWPage.ui'
#
# Created: Sun Jan  8 16:42:19 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ETHSWPage(object):
    def setupUi(self, ETHSWPage):
        ETHSWPage.setObjectName(_fromUtf8("ETHSWPage"))
        ETHSWPage.resize(397, 315)
        ETHSWPage.setWindowTitle(QtGui.QApplication.translate("ETHSWPage", "Ethernet Switch", None, QtGui.QApplication.UnicodeUTF8))
        self.gridlayout = QtGui.QGridLayout(ETHSWPage)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.groupBox = QtGui.QGroupBox(ETHSWPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(QtGui.QApplication.translate("ETHSWPage", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("ETHSWPage", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 1)
        self.spinBoxPort = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxPort.sizePolicy().hasHeightForWidth())
        self.spinBoxPort.setSizePolicy(sizePolicy)
        self.spinBoxPort.setMinimum(0)
        self.spinBoxPort.setMaximum(65535)
        self.spinBoxPort.setProperty("value", 1)
        self.spinBoxPort.setObjectName(_fromUtf8("spinBoxPort"))
        self.gridlayout1.addWidget(self.spinBoxPort, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("ETHSWPage", "VLAN:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout1.addWidget(self.label_3, 1, 0, 1, 1)
        self.spinBoxVLAN = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxVLAN.sizePolicy().hasHeightForWidth())
        self.spinBoxVLAN.setSizePolicy(sizePolicy)
        self.spinBoxVLAN.setMinimum(0)
        self.spinBoxVLAN.setMaximum(65535)
        self.spinBoxVLAN.setProperty("value", 1)
        self.spinBoxVLAN.setObjectName(_fromUtf8("spinBoxVLAN"))
        self.gridlayout1.addWidget(self.spinBoxVLAN, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("ETHSWPage", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout1.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBoxPortType = QtGui.QComboBox(self.groupBox)
        self.comboBoxPortType.setObjectName(_fromUtf8("comboBoxPortType"))
        self.comboBoxPortType.addItem(_fromUtf8(""))
        self.comboBoxPortType.setItemText(0, QtGui.QApplication.translate("ETHSWPage", "access", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPortType.addItem(_fromUtf8(""))
        self.comboBoxPortType.setItemText(1, QtGui.QApplication.translate("ETHSWPage", "dot1q", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPortType.addItem(_fromUtf8(""))
        self.comboBoxPortType.setItemText(2, QtGui.QApplication.translate("ETHSWPage", "qinq", None, QtGui.QApplication.UnicodeUTF8))
        self.gridlayout1.addWidget(self.comboBoxPortType, 2, 1, 1, 1)
        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(ETHSWPage)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ETHSWPage", "Ports", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.treeWidgetPorts = QtGui.QTreeWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidgetPorts.sizePolicy().hasHeightForWidth())
        self.treeWidgetPorts.setSizePolicy(sizePolicy)
        self.treeWidgetPorts.setRootIsDecorated(False)
        self.treeWidgetPorts.setObjectName(_fromUtf8("treeWidgetPorts"))
        self.treeWidgetPorts.headerItem().setText(0, QtGui.QApplication.translate("ETHSWPage", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetPorts.headerItem().setText(1, QtGui.QApplication.translate("ETHSWPage", "VLAN", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetPorts.headerItem().setText(2, QtGui.QApplication.translate("ETHSWPage", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.vboxlayout.addWidget(self.treeWidgetPorts)
        self.gridlayout.addWidget(self.groupBox_2, 0, 2, 3, 1)
        self.pushButtonAdd = QtGui.QPushButton(ETHSWPage)
        self.pushButtonAdd.setText(QtGui.QApplication.translate("ETHSWPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.gridlayout.addWidget(self.pushButtonAdd, 1, 0, 1, 1)
        self.pushButtonDelete = QtGui.QPushButton(ETHSWPage)
        self.pushButtonDelete.setEnabled(False)
        self.pushButtonDelete.setText(QtGui.QApplication.translate("ETHSWPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.gridlayout.addWidget(self.pushButtonDelete, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 71, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1, 3, 2, 1, 1)

        self.retranslateUi(ETHSWPage)
        QtCore.QMetaObject.connectSlotsByName(ETHSWPage)
        ETHSWPage.setTabOrder(self.spinBoxPort, self.spinBoxVLAN)
        ETHSWPage.setTabOrder(self.spinBoxVLAN, self.comboBoxPortType)
        ETHSWPage.setTabOrder(self.comboBoxPortType, self.pushButtonAdd)
        ETHSWPage.setTabOrder(self.pushButtonAdd, self.pushButtonDelete)
        ETHSWPage.setTabOrder(self.pushButtonDelete, self.treeWidgetPorts)

    def retranslateUi(self, ETHSWPage):
        pass

