# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_FWPage.ui'
#
# Created: Fri Feb  5 18:22:14 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FWPage(object):
    def setupUi(self, FWPage):
        FWPage.setObjectName("FWPage")
        FWPage.resize(419, 453)
        self.gridLayout = QtGui.QGridLayout(FWPage)
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtGui.QLabel(FWPage)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEditImage = QtGui.QLineEdit(FWPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditImage.sizePolicy().hasHeightForWidth())
        self.lineEditImage.setSizePolicy(sizePolicy)
        self.lineEditImage.setObjectName("lineEditImage")
        self.gridLayout.addWidget(self.lineEditImage, 0, 2, 1, 1)
        self.pushButtonImageBrowser = QtGui.QPushButton(FWPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImageBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonImageBrowser.setSizePolicy(sizePolicy)
        self.pushButtonImageBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonImageBrowser.setObjectName("pushButtonImageBrowser")
        self.gridLayout.addWidget(self.pushButtonImageBrowser, 0, 3, 1, 1)
        self.label_24 = QtGui.QLabel(FWPage)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 1, 0, 1, 1)
        self.spinBoxRamSize = QtGui.QSpinBox(FWPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setMaximum(100000)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty("value", 128)
        self.spinBoxRamSize.setObjectName("spinBoxRamSize")
        self.gridLayout.addWidget(self.spinBoxRamSize, 1, 2, 1, 2)
        self.label_26 = QtGui.QLabel(FWPage)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 2, 0, 1, 1)
        self.comboBoxNIC = QtGui.QComboBox(FWPage)
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
        self.gridLayout.addWidget(self.comboBoxNIC, 2, 2, 1, 2)
        self.label_8 = QtGui.QLabel(FWPage)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 2)
        self.lineEditOptions = QtGui.QLineEdit(FWPage)
        self.lineEditOptions.setEnabled(True)
        self.lineEditOptions.setObjectName("lineEditOptions")
        self.gridLayout.addWidget(self.lineEditOptions, 3, 2, 1, 2)
        self.checkBoxKqemu = QtGui.QCheckBox(FWPage)
        self.checkBoxKqemu.setEnabled(True)
        self.checkBoxKqemu.setObjectName("checkBoxKqemu")
        self.gridLayout.addWidget(self.checkBoxKqemu, 4, 0, 1, 3)
        self.label_20 = QtGui.QLabel(FWPage)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.lineEditKey = QtGui.QLineEdit(FWPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditKey.sizePolicy().hasHeightForWidth())
        self.lineEditKey.setSizePolicy(sizePolicy)
        self.lineEditKey.setObjectName("lineEditKey")
        self.gridLayout.addWidget(self.lineEditKey, 5, 2, 1, 2)
        self.label_21 = QtGui.QLabel(FWPage)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 6, 0, 1, 1)
        self.lineEditSerial = QtGui.QLineEdit(FWPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSerial.sizePolicy().hasHeightForWidth())
        self.lineEditSerial.setSizePolicy(sizePolicy)
        self.lineEditSerial.setObjectName("lineEditSerial")
        self.gridLayout.addWidget(self.lineEditSerial, 6, 2, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)

        self.retranslateUi(FWPage)
        self.comboBoxNIC.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(FWPage)

    def retranslateUi(self, FWPage):
        FWPage.setWindowTitle(QtGui.QApplication.translate("FWPage", "Firewall configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("FWPage", "PIX Image:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImageBrowser.setText(QtGui.QApplication.translate("FWPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("FWPage", "RAM size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("FWPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("FWPage", "NIC:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(0, QtGui.QApplication.translate("FWPage", "ne2k_pci", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(1, QtGui.QApplication.translate("FWPage", "i82551", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(2, QtGui.QApplication.translate("FWPage", "i82557b", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(3, QtGui.QApplication.translate("FWPage", "i82559er", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(4, QtGui.QApplication.translate("FWPage", "rtl8139", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(5, QtGui.QApplication.translate("FWPage", "e1000", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(6, QtGui.QApplication.translate("FWPage", "pcnet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(7, QtGui.QApplication.translate("FWPage", "virtio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("FWPage", "Qemu Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKqemu.setText(QtGui.QApplication.translate("FWPage", "Use KQemu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("FWPage", "Key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("FWPage", "Serial:", None, QtGui.QApplication.UnicodeUTF8))

