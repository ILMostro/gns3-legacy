# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:

# Form implementation generated from reading ui file './ConfigurationPages/Form_JunOSPage.ui'
#
# Created: Wed Sep 28 16:25:07 2011
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_JunOSPage(object):
    def setupUi(self, JunOSPage):
        JunOSPage.setObjectName(_fromUtf8("JunOSPage"))
        JunOSPage.resize(419, 453)
        self.gridLayout = QtGui.QGridLayout(JunOSPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_17 = QtGui.QLabel(JunOSPage)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEditImage = QtGui.QLineEdit(JunOSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditImage.sizePolicy().hasHeightForWidth())
        self.lineEditImage.setSizePolicy(sizePolicy)
        self.lineEditImage.setObjectName(_fromUtf8("lineEditImage"))
        self.gridLayout.addWidget(self.lineEditImage, 0, 1, 1, 1)
        self.pushButtonImageBrowser = QtGui.QPushButton(JunOSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImageBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonImageBrowser.setSizePolicy(sizePolicy)
        self.pushButtonImageBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonImageBrowser.setObjectName(_fromUtf8("pushButtonImageBrowser"))
        self.gridLayout.addWidget(self.pushButtonImageBrowser, 0, 2, 1, 1)
        self.label_24 = QtGui.QLabel(JunOSPage)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 1, 0, 1, 1)
        self.spinBoxRamSize = QtGui.QSpinBox(JunOSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setMaximum(100000)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty(_fromUtf8("value"), 96)
        self.spinBoxRamSize.setObjectName(_fromUtf8("spinBoxRamSize"))
        self.gridLayout.addWidget(self.spinBoxRamSize, 1, 1, 1, 2)
        self.label_37 = QtGui.QLabel(JunOSPage)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout.addWidget(self.label_37, 2, 0, 1, 1)
        self.spinBoxNics = QtGui.QSpinBox(JunOSPage)
        self.spinBoxNics.setMinimum(0)
        self.spinBoxNics.setMaximum(100000)
        self.spinBoxNics.setSingleStep(1)
        self.spinBoxNics.setProperty(_fromUtf8("value"), 6)
        self.spinBoxNics.setObjectName(_fromUtf8("spinBoxNics"))
        self.gridLayout.addWidget(self.spinBoxNics, 2, 1, 1, 2)
        self.label_26 = QtGui.QLabel(JunOSPage)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 3, 0, 1, 1)
        self.comboBoxNIC = QtGui.QComboBox(JunOSPage)
        self.comboBoxNIC.setEnabled(True)
        self.comboBoxNIC.setObjectName(_fromUtf8("comboBoxNIC"))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBoxNIC, 3, 1, 1, 2)
        self.label_8 = QtGui.QLabel(JunOSPage)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.lineEditOptions = QtGui.QLineEdit(JunOSPage)
        self.lineEditOptions.setEnabled(True)
        self.lineEditOptions.setObjectName(_fromUtf8("lineEditOptions"))
        self.gridLayout.addWidget(self.lineEditOptions, 4, 1, 1, 2)
        self.checkBoxKqemu = QtGui.QCheckBox(JunOSPage)
        self.checkBoxKqemu.setEnabled(True)
        self.checkBoxKqemu.setObjectName(_fromUtf8("checkBoxKqemu"))
        self.gridLayout.addWidget(self.checkBoxKqemu, 5, 0, 1, 1)
        self.checkBoxKVM = QtGui.QCheckBox(JunOSPage)
        self.checkBoxKVM.setEnabled(True)
        self.checkBoxKVM.setObjectName(_fromUtf8("checkBoxKVM"))
        self.gridLayout.addWidget(self.checkBoxKVM, 6, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)

        self.retranslateUi(JunOSPage)
        self.comboBoxNIC.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(JunOSPage)

    def retranslateUi(self, JunOSPage):
        JunOSPage.setWindowTitle(QtGui.QApplication.translate("JunOSPage", "JunOS configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("JunOSPage", "JunOS Image:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImageBrowser.setText(QtGui.QApplication.translate("JunOSPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("JunOSPage", "RAM:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("JunOSPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("JunOSPage", "Number of NICs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("JunOSPage", "NIC model:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(0, QtGui.QApplication.translate("JunOSPage", "ne2k_pci", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(1, QtGui.QApplication.translate("JunOSPage", "i82551", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(2, QtGui.QApplication.translate("JunOSPage", "i82557b", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(3, QtGui.QApplication.translate("JunOSPage", "i82559er", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(4, QtGui.QApplication.translate("JunOSPage", "rtl8139", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(5, QtGui.QApplication.translate("JunOSPage", "e1000", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(6, QtGui.QApplication.translate("JunOSPage", "pcnet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(7, QtGui.QApplication.translate("JunOSPage", "virtio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("JunOSPage", "Qemu Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKqemu.setText(QtGui.QApplication.translate("JunOSPage", "Use KQemu", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKVM.setText(QtGui.QApplication.translate("JunOSPage", "Use KVM (Linux only)", None, QtGui.QApplication.UnicodeUTF8))

