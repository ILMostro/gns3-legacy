# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Wed Sep 26 18:58:44 2007
#      by: PyQt4 UI code generator 4-snapshot-20070701
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_SwitchMode = QtGui.QAction(MainWindow)
        self.action_SwitchMode.setIcon(QtGui.QIcon(":/icons/view-refresh.svg"))
        self.action_SwitchMode.setObjectName("action_SwitchMode")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_General.addAction(self.action_SwitchMode)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SwitchMode.setText(QtGui.QApplication.translate("MainWindow", "Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Sun Oct 14 19:23:32 2007
#      by: PyQt4 UI code generator 4-snapshot-20070710
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_SwitchMode = QtGui.QAction(MainWindow)
        self.action_SwitchMode.setIcon(QtGui.QIcon(":/icons/view-refresh.svg"))
        self.action_SwitchMode.setObjectName("action_SwitchMode")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_General.addAction(self.action_SwitchMode)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SwitchMode.setText(QtGui.QApplication.translate("MainWindow", "Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Sun Oct 14 19:33:15 2007
#      by: PyQt4 UI code generator 4-snapshot-20070710
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_SwitchMode = QtGui.QAction(MainWindow)
        self.action_SwitchMode.setIcon(QtGui.QIcon(":/icons/view-refresh.svg"))
        self.action_SwitchMode.setObjectName("action_SwitchMode")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_General.addAction(self.action_SwitchMode)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SwitchMode.setText(QtGui.QApplication.translate("MainWindow", "Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Sun Oct 14 19:33:52 2007
#      by: PyQt4 UI code generator 4-snapshot-20070710
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_SwitchMode = QtGui.QAction(MainWindow)
        self.action_SwitchMode.setIcon(QtGui.QIcon(":/icons/view-refresh.svg"))
        self.action_SwitchMode.setObjectName("action_SwitchMode")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_General.addAction(self.action_SwitchMode)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SwitchMode.setText(QtGui.QApplication.translate("MainWindow", "Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Sun Oct 14 19:43:25 2007
#      by: PyQt4 UI code generator 4-snapshot-20070710
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_SwitchMode = QtGui.QAction(MainWindow)
        self.action_SwitchMode.setIcon(QtGui.QIcon(":/icons/view-refresh.svg"))
        self.action_SwitchMode.setObjectName("action_SwitchMode")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_General.addAction(self.action_SwitchMode)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SwitchMode.setText(QtGui.QApplication.translate("MainWindow", "Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Thu Nov  1 11:59:19 2007
#      by: PyQt4 UI code generator 4-snapshot-20070710
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Thu Nov  1 14:59:08 2007
#      by: PyQt4 UI code generator 4-snapshot-20070710
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Fri Feb  1 15:12:44 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Fri Feb  1 15:14:57 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Fri Feb  1 15:59:48 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Sat Feb  2 11:32:32 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Sat Feb  2 11:38:24 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWindow.ui'
#
# Created: Wed Feb  6 16:51:25 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,840,600).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/images/logo_icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.graphicsView = Scene(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridlayout.addWidget(self.graphicsView,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,840,25))
        self.menubar.setObjectName("menubar")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar_General = QtGui.QToolBar(MainWindow)
        self.toolBar_General.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_General.setObjectName("toolBar_General")
        MainWindow.addToolBar(self.toolBar_General)

        self.dockWidget_NodeTypes = QtGui.QDockWidget(MainWindow)
        self.dockWidget_NodeTypes.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_NodeTypes.setObjectName("dockWidget_NodeTypes")

        self.dockWidgetContents_NodeTypes = QtGui.QWidget(self.dockWidget_NodeTypes)
        self.dockWidgetContents_NodeTypes.setObjectName("dockWidgetContents_NodeTypes")

        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_NodeTypes)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nodesDock = nodesDock(self.dockWidgetContents_NodeTypes)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesDock.sizePolicy().hasHeightForWidth())
        self.nodesDock.setSizePolicy(sizePolicy)
        self.nodesDock.setIconSize(QtCore.QSize(24,24))
        self.nodesDock.setRootIsDecorated(False)
        self.nodesDock.setObjectName("nodesDock")
        self.vboxlayout.addWidget(self.nodesDock)
        self.dockWidget_NodeTypes.setWidget(self.dockWidgetContents_NodeTypes)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockWidget_NodeTypes)

        self.toolBar_Design = QtGui.QToolBar(MainWindow)
        self.toolBar_Design.setObjectName("toolBar_Design")
        MainWindow.addToolBar(self.toolBar_Design)

        self.toolBar_Emulation = QtGui.QToolBar(MainWindow)
        self.toolBar_Emulation.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_Emulation.setObjectName("toolBar_Emulation")
        MainWindow.addToolBar(self.toolBar_Emulation)

        self.dockWidget_TopoSum = QtGui.QDockWidget(MainWindow)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_TopoSum.sizePolicy().hasHeightForWidth())
        self.dockWidget_TopoSum.setSizePolicy(sizePolicy)
        self.dockWidget_TopoSum.setMinimumSize(QtCore.QSize(50,0))
        self.dockWidget_TopoSum.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.NoDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_TopoSum.setObjectName("dockWidget_TopoSum")

        self.dockWidgetContents_7 = QtGui.QWidget(self.dockWidget_TopoSum)
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")

        self.gridlayout1 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.treeWidget_TopologySummary = topologySummaryDock(self.dockWidgetContents_7)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_TopologySummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_TopologySummary.setSizePolicy(sizePolicy)
        self.treeWidget_TopologySummary.setObjectName("treeWidget_TopologySummary")
        self.gridlayout1.addWidget(self.treeWidget_TopologySummary,0,0,1,1)
        self.dockWidget_TopoSum.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),self.dockWidget_TopoSum)

        self.dockWidget_Console = QtGui.QDockWidget(MainWindow)
        self.dockWidget_Console.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockWidget_Console.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_Console.setObjectName("dockWidget_Console")

        self.dockWidgetContents_5 = QtGui.QWidget(self.dockWidget_Console)
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textEditConsole = Console(self.dockWidgetContents_5)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setObjectName("textEditConsole")
        self.vboxlayout1.addWidget(self.textEditConsole)
        self.dockWidget_Console.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),self.dockWidget_Console)

        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName("action_About")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/open.svg"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/save.svg"))
        self.action_Save.setObjectName("action_Save")

        self.action_Add_link = QtGui.QAction(MainWindow)
        self.action_Add_link.setCheckable(True)
        self.action_Add_link.setIcon(QtGui.QIcon(":/icons/connection.svg"))
        self.action_Add_link.setObjectName("action_Add_link")

        self.action_IOS_images = QtGui.QAction(MainWindow)
        self.action_IOS_images.setObjectName("action_IOS_images")

        self.action_OnlineHelp = QtGui.QAction(MainWindow)
        self.action_OnlineHelp.setEnabled(False)
        self.action_OnlineHelp.setObjectName("action_OnlineHelp")

        self.action_Export = QtGui.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")

        self.action_StartAll = QtGui.QAction(MainWindow)
        self.action_StartAll.setEnabled(True)
        self.action_StartAll.setIcon(QtGui.QIcon(":/icons/start_metal.svg"))
        self.action_StartAll.setObjectName("action_StartAll")

        self.action_StopAll = QtGui.QAction(MainWindow)
        self.action_StopAll.setEnabled(True)
        self.action_StopAll.setIcon(QtGui.QIcon(":/icons/stop_metal.svg"))
        self.action_StopAll.setObjectName("action_StopAll")

        self.action_ShowHostnames = QtGui.QAction(MainWindow)
        self.action_ShowHostnames.setCheckable(True)
        self.action_ShowHostnames.setIcon(QtGui.QIcon(":/icons/show-hostname.svg"))
        self.action_ShowHostnames.setObjectName("action_ShowHostnames")

        self.action_TelnetAll = QtGui.QAction(MainWindow)
        self.action_TelnetAll.setEnabled(True)
        self.action_TelnetAll.setIcon(QtGui.QIcon(":/icons/console.svg"))
        self.action_TelnetAll.setObjectName("action_TelnetAll")

        self.action_Design_Mode = QtGui.QAction(MainWindow)
        self.action_Design_Mode.setObjectName("action_Design_Mode")

        self.action_Emulation_Mode = QtGui.QAction(MainWindow)
        self.action_Emulation_Mode.setObjectName("action_Emulation_Mode")

        self.action_Simulation_Mode = QtGui.QAction(MainWindow)
        self.action_Simulation_Mode.setObjectName("action_Simulation_Mode")

        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setIcon(QtGui.QIcon(":/icons/save-as.svg"))
        self.action_SaveAs.setObjectName("action_SaveAs")

        self.action_New_Project = QtGui.QAction(MainWindow)
        self.action_New_Project.setEnabled(False)
        self.action_New_Project.setObjectName("action_New_Project")

        self.action_AboutQt = QtGui.QAction(MainWindow)
        self.action_AboutQt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.action_AboutQt.setObjectName("action_AboutQt")

        self.action_ZoomIn = QtGui.QAction(MainWindow)
        self.action_ZoomIn.setObjectName("action_ZoomIn")

        self.action_ZoomOut = QtGui.QAction(MainWindow)
        self.action_ZoomOut.setObjectName("action_ZoomOut")

        self.action_ZoomReset = QtGui.QAction(MainWindow)
        self.action_ZoomReset.setObjectName("action_ZoomReset")

        self.action_ZoomFit = QtGui.QAction(MainWindow)
        self.action_ZoomFit.setEnabled(False)
        self.action_ZoomFit.setObjectName("action_ZoomFit")

        self.action_SelectAll = QtGui.QAction(MainWindow)
        self.action_SelectAll.setObjectName("action_SelectAll")

        self.action_SelectNone = QtGui.QAction(MainWindow)
        self.action_SelectNone.setObjectName("action_SelectNone")

        self.action_Preferences = QtGui.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")

        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setEnabled(False)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setEnabled(False)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setEnabled(False)
        self.action_Paste.setObjectName("action_Paste")

        self.action_SuspendAll = QtGui.QAction(MainWindow)
        self.action_SuspendAll.setIcon(QtGui.QIcon(":/icons/pause_metal.svg"))
        self.action_SuspendAll.setObjectName("action_SuspendAll")
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_SelectAll)
        self.menu_Edit.addAction(self.action_SelectNone)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_IOS_images)
        self.menu_Edit.addAction(self.action_Preferences)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Export)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_OnlineHelp)
        self.menu_About.addAction(self.action_AboutQt)
        self.menu_About.addAction(self.action_About)
        self.menu_View.addAction(self.action_ZoomIn)
        self.menu_View.addAction(self.action_ZoomOut)
        self.menu_View.addAction(self.action_ZoomReset)
        self.menu_View.addAction(self.action_ZoomFit)
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar_General.addAction(self.action_Open)
        self.toolBar_General.addAction(self.action_Save)
        self.toolBar_General.addAction(self.action_SaveAs)
        self.toolBar_General.addSeparator()
        self.toolBar_General.addAction(self.action_ShowHostnames)
        self.toolBar_Design.addAction(self.action_Add_link)
        self.toolBar_Emulation.addAction(self.action_TelnetAll)
        self.toolBar_Emulation.addAction(self.action_StartAll)
        self.toolBar_Emulation.addAction(self.action_SuspendAll)
        self.toolBar_Emulation.addAction(self.action_StopAll)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit,QtCore.SIGNAL("activated()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GNS3", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_About.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_General.setWindowTitle(QtGui.QApplication.translate("MainWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_NodeTypes.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nodes Types", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesDock.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Design.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Emulation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_TopoSum.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topology Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_TopologySummary.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setIconText(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_link.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a link", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setText(QtGui.QApplication.translate("MainWindow", "IOS images and hypervisors", None, QtGui.QApplication.UnicodeUTF8))
        self.action_IOS_images.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OnlineHelp.setText(QtGui.QApplication.translate("MainWindow", "&Online Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Export.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setText(QtGui.QApplication.translate("MainWindow", "Start/Resume all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StartAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start or resume all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setText(QtGui.QApplication.translate("MainWindow", "Stop all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_StopAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop all IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setText(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowHostnames.setToolTip(QtGui.QApplication.translate("MainWindow", "Show hostnames", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setText(QtGui.QApplication.translate("MainWindow", "Telnet all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_TelnetAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start a console on all running IOS instances", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Design_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Design Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Emulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Emulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Simulation_Mode.setText(QtGui.QApplication.translate("MainWindow", "&Simulation Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setIconText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setToolTip(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_Project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AboutQt.setText(QtGui.QApplication.translate("MainWindow", "About &Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setText(QtGui.QApplication.translate("MainWindow", "Zoom &1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomReset.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+/", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomFit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setText(QtGui.QApplication.translate("MainWindow", "Select &None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SelectNone.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setText(QtGui.QApplication.translate("MainWindow", "Suspend all IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SuspendAll.setStatusTip(QtGui.QApplication.translate("MainWindow", "Suspend all IOS instances", None, QtGui.QApplication.UnicodeUTF8))

from GNS3.Console import Console
from GNS3.Ui.Widget_topologySummaryDock import topologySummaryDock
from GNS3.Ui.Widget_nodesDock import nodesDock
from GNS3.Scene import Scene
import svg_resources_rc
