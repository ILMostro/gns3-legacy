# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_JunOSPage.ui'
#
# Created: Fri Jun 11 11:25:55 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_JunOSPage(object):
    def setupUi(self, JunOSPage):
        JunOSPage.setObjectName("JunOSPage")
        JunOSPage.resize(419, 453)
        self.gridLayout = QtGui.QGridLayout(JunOSPage)
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtGui.QLabel(JunOSPage)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEditImage = QtGui.QLineEdit(JunOSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditImage.sizePolicy().hasHeightForWidth())
        self.lineEditImage.setSizePolicy(sizePolicy)
        self.lineEditImage.setObjectName("lineEditImage")
        self.gridLayout.addWidget(self.lineEditImage, 0, 1, 1, 1)
        self.pushButtonImageBrowser = QtGui.QPushButton(JunOSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImageBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonImageBrowser.setSizePolicy(sizePolicy)
        self.pushButtonImageBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonImageBrowser.setObjectName("pushButtonImageBrowser")
        self.gridLayout.addWidget(self.pushButtonImageBrowser, 0, 2, 1, 1)
        self.label_24 = QtGui.QLabel(JunOSPage)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 1, 0, 1, 1)
        self.spinBoxRamSize = QtGui.QSpinBox(JunOSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setMaximum(100000)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty("value", 96)
        self.spinBoxRamSize.setObjectName("spinBoxRamSize")
        self.gridLayout.addWidget(self.spinBoxRamSize, 1, 1, 1, 2)
        self.label_26 = QtGui.QLabel(JunOSPage)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 2, 0, 1, 1)
        self.comboBoxNIC = QtGui.QComboBox(JunOSPage)
        self.comboBoxNIC.setEnabled(True)
        self.comboBoxNIC.setObjectName("comboBoxNIC")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.gridLayout.addWidget(self.comboBoxNIC, 2, 1, 1, 2)
        self.label_8 = QtGui.QLabel(JunOSPage)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lineEditOptions = QtGui.QLineEdit(JunOSPage)
        self.lineEditOptions.setEnabled(True)
        self.lineEditOptions.setObjectName("lineEditOptions")
        self.gridLayout.addWidget(self.lineEditOptions, 3, 1, 1, 2)
        self.checkBoxKqemu = QtGui.QCheckBox(JunOSPage)
        self.checkBoxKqemu.setEnabled(True)
        self.checkBoxKqemu.setObjectName("checkBoxKqemu")
        self.gridLayout.addWidget(self.checkBoxKqemu, 4, 0, 1, 1)
        self.checkBoxKVM = QtGui.QCheckBox(JunOSPage)
        self.checkBoxKVM.setEnabled(True)
        self.checkBoxKVM.setObjectName("checkBoxKVM")
        self.gridLayout.addWidget(self.checkBoxKVM, 5, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)

        self.retranslateUi(JunOSPage)
        self.comboBoxNIC.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(JunOSPage)

    def retranslateUi(self, JunOSPage):
        JunOSPage.setWindowTitle(QtGui.QApplication.translate("JunOSPage", "Firewall configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("JunOSPage", "JunOS Image:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImageBrowser.setText(QtGui.QApplication.translate("JunOSPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("JunOSPage", "RAM size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("JunOSPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("JunOSPage", "NIC:", None, QtGui.QApplication.UnicodeUTF8))
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

