# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_DecorativeNodePage.ui'
#
# Created: Thu Apr 17 22:48:55 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DecorativeNodePage(object):
    def setupUi(self, DecorativeNodePage):
        DecorativeNodePage.setObjectName("DecorativeNodePage")
        DecorativeNodePage.resize(QtCore.QSize(QtCore.QRect(0,0,433,443).size()).expandedTo(DecorativeNodePage.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(DecorativeNodePage)
        self.gridlayout.setObjectName("gridlayout")

        self.groupBox_11 = QtGui.QGroupBox(DecorativeNodePage)
        self.groupBox_11.setObjectName("groupBox_11")

        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_11)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_9 = QtGui.QLabel(self.groupBox_11)
        self.label_9.setObjectName("label_9")
        self.gridlayout1.addWidget(self.label_9,0,0,1,1)

        self.lineEditInterface = QtGui.QLineEdit(self.groupBox_11)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditInterface.sizePolicy().hasHeightForWidth())
        self.lineEditInterface.setSizePolicy(sizePolicy)
        self.lineEditInterface.setObjectName("lineEditInterface")
        self.gridlayout1.addWidget(self.lineEditInterface,1,0,1,1)
        self.gridlayout.addWidget(self.groupBox_11,0,0,1,2)

        self.groupBox_10 = QtGui.QGroupBox(DecorativeNodePage)
        self.groupBox_10.setObjectName("groupBox_10")

        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox_10)
        self.vboxlayout.setObjectName("vboxlayout")

        self.listWidgetInterfaces = QtGui.QListWidget(self.groupBox_10)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetInterfaces.sizePolicy().hasHeightForWidth())
        self.listWidgetInterfaces.setSizePolicy(sizePolicy)
        self.listWidgetInterfaces.setObjectName("listWidgetInterfaces")
        self.vboxlayout.addWidget(self.listWidgetInterfaces)
        self.gridlayout.addWidget(self.groupBox_10,0,2,3,1)

        self.pushButtonAddInterface = QtGui.QPushButton(DecorativeNodePage)
        self.pushButtonAddInterface.setObjectName("pushButtonAddInterface")
        self.gridlayout.addWidget(self.pushButtonAddInterface,1,0,1,1)

        self.pushButtonDeleteInterface = QtGui.QPushButton(DecorativeNodePage)
        self.pushButtonDeleteInterface.setEnabled(False)
        self.pushButtonDeleteInterface.setObjectName("pushButtonDeleteInterface")
        self.gridlayout.addWidget(self.pushButtonDeleteInterface,1,1,1,1)

        spacerItem = QtGui.QSpacerItem(20,321,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem,2,0,2,2)

        spacerItem1 = QtGui.QSpacerItem(20,221,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1,3,2,1,1)

        self.retranslateUi(DecorativeNodePage)
        QtCore.QMetaObject.connectSlotsByName(DecorativeNodePage)
        DecorativeNodePage.setTabOrder(self.lineEditInterface,self.pushButtonAddInterface)
        DecorativeNodePage.setTabOrder(self.pushButtonAddInterface,self.pushButtonDeleteInterface)
        DecorativeNodePage.setTabOrder(self.pushButtonDeleteInterface,self.listWidgetInterfaces)

    def retranslateUi(self, DecorativeNodePage):
        DecorativeNodePage.setWindowTitle(QtGui.QApplication.translate("DecorativeNodePage", "Decorative Node", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setTitle(QtGui.QApplication.translate("DecorativeNodePage", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DecorativeNodePage", "Interface name:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("DecorativeNodePage", "Interfaces", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddInterface.setText(QtGui.QApplication.translate("DecorativeNodePage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteInterface.setText(QtGui.QApplication.translate("DecorativeNodePage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))

