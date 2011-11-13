# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_ASAPage.ui'
#
# Created: Sat Nov 12 17:10:00 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ASAPage(object):
    def setupUi(self, ASAPage):
        ASAPage.setObjectName(_fromUtf8("ASAPage"))
        ASAPage.resize(419, 453)
        ASAPage.setWindowTitle(QtGui.QApplication.translate("ASAPage", "Firewall configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(ASAPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_24 = QtGui.QLabel(ASAPage)
        self.label_24.setText(QtGui.QApplication.translate("ASAPage", "RAM:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)
        self.spinBoxRamSize = QtGui.QSpinBox(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("ASAPage", " MiB", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setMaximum(100000)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty("value", 256)
        self.spinBoxRamSize.setObjectName(_fromUtf8("spinBoxRamSize"))
        self.gridLayout.addWidget(self.spinBoxRamSize, 0, 1, 1, 2)
        self.label_37 = QtGui.QLabel(ASAPage)
        self.label_37.setText(QtGui.QApplication.translate("ASAPage", "Number of NICs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout.addWidget(self.label_37, 1, 0, 1, 1)
        self.spinBoxNics = QtGui.QSpinBox(ASAPage)
        self.spinBoxNics.setMinimum(0)
        self.spinBoxNics.setMaximum(100000)
        self.spinBoxNics.setSingleStep(1)
        self.spinBoxNics.setProperty("value", 6)
        self.spinBoxNics.setObjectName(_fromUtf8("spinBoxNics"))
        self.gridLayout.addWidget(self.spinBoxNics, 1, 1, 1, 2)
        self.label_26 = QtGui.QLabel(ASAPage)
        self.label_26.setText(QtGui.QApplication.translate("ASAPage", "NIC model:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 2, 0, 1, 1)
        self.comboBoxNIC = QtGui.QComboBox(ASAPage)
        self.comboBoxNIC.setEnabled(True)
        self.comboBoxNIC.setObjectName(_fromUtf8("comboBoxNIC"))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(0, QtGui.QApplication.translate("ASAPage", "ne2k_pci", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(1, QtGui.QApplication.translate("ASAPage", "i82551", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(2, QtGui.QApplication.translate("ASAPage", "i82557b", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(3, QtGui.QApplication.translate("ASAPage", "i82559er", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(4, QtGui.QApplication.translate("ASAPage", "rtl8139", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(5, QtGui.QApplication.translate("ASAPage", "e1000", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(6, QtGui.QApplication.translate("ASAPage", "pcnet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(7, QtGui.QApplication.translate("ASAPage", "virtio", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.comboBoxNIC, 2, 1, 1, 2)
        self.label_8 = QtGui.QLabel(ASAPage)
        self.label_8.setText(QtGui.QApplication.translate("ASAPage", "Qemu Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lineEditOptions = QtGui.QLineEdit(ASAPage)
        self.lineEditOptions.setEnabled(True)
        self.lineEditOptions.setObjectName(_fromUtf8("lineEditOptions"))
        self.gridLayout.addWidget(self.lineEditOptions, 3, 1, 1, 2)
        self.label_20 = QtGui.QLabel(ASAPage)
        self.label_20.setText(QtGui.QApplication.translate("ASAPage", "Initrd:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 6, 0, 1, 1)
        self.lineEditInitrd = QtGui.QLineEdit(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditInitrd.sizePolicy().hasHeightForWidth())
        self.lineEditInitrd.setSizePolicy(sizePolicy)
        self.lineEditInitrd.setObjectName(_fromUtf8("lineEditInitrd"))
        self.gridLayout.addWidget(self.lineEditInitrd, 6, 1, 2, 1)
        self.pushButtonInitrdBrowser = QtGui.QPushButton(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInitrdBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonInitrdBrowser.setSizePolicy(sizePolicy)
        self.pushButtonInitrdBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonInitrdBrowser.setText(QtGui.QApplication.translate("ASAPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonInitrdBrowser.setObjectName(_fromUtf8("pushButtonInitrdBrowser"))
        self.gridLayout.addWidget(self.pushButtonInitrdBrowser, 6, 2, 1, 1)
        self.pushButtonKernelBrowser = QtGui.QPushButton(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKernelBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonKernelBrowser.setSizePolicy(sizePolicy)
        self.pushButtonKernelBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonKernelBrowser.setText(QtGui.QApplication.translate("ASAPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonKernelBrowser.setObjectName(_fromUtf8("pushButtonKernelBrowser"))
        self.gridLayout.addWidget(self.pushButtonKernelBrowser, 7, 2, 2, 1)
        self.label_21 = QtGui.QLabel(ASAPage)
        self.label_21.setText(QtGui.QApplication.translate("ASAPage", "Kernel:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout.addWidget(self.label_21, 8, 0, 1, 1)
        self.lineEditKernel = QtGui.QLineEdit(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditKernel.sizePolicy().hasHeightForWidth())
        self.lineEditKernel.setSizePolicy(sizePolicy)
        self.lineEditKernel.setObjectName(_fromUtf8("lineEditKernel"))
        self.gridLayout.addWidget(self.lineEditKernel, 8, 1, 1, 1)
        self.label_13 = QtGui.QLabel(ASAPage)
        self.label_13.setText(QtGui.QApplication.translate("ASAPage", "Kernel cmd line:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)
        self.lineEditKernelCmdLine = QtGui.QLineEdit(ASAPage)
        self.lineEditKernelCmdLine.setObjectName(_fromUtf8("lineEditKernelCmdLine"))
        self.gridLayout.addWidget(self.lineEditKernelCmdLine, 9, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 3)
        self.checkBoxKVM = QtGui.QCheckBox(ASAPage)
        self.checkBoxKVM.setEnabled(True)
        self.checkBoxKVM.setText(QtGui.QApplication.translate("ASAPage", "Use KVM", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKVM.setObjectName(_fromUtf8("checkBoxKVM"))
        self.gridLayout.addWidget(self.checkBoxKVM, 5, 0, 1, 1)

        self.retranslateUi(ASAPage)
        self.comboBoxNIC.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(ASAPage)

    def retranslateUi(self, ASAPage):
        pass

