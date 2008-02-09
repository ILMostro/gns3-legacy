# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:
#
# Copyright (C) 2007 GNS-3 Dev Team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# Contact: contact@gns3.net
#

import re
import GNS3.Dynagen.dynamips_lib as lib
import GNS3.Dynagen.dynagen as dynagen
import GNS3.Globals as globals
from GNS3.Node.AbstractNode import AbstractNode
from PyQt4 import QtCore, QtGui
from GNS3.Utils import translate

atm_id = 0
MAPVCI = re.compile(r"""^([0-9]*):([0-9]*):([0-9]*)$""")

class ATMSW(AbstractNode):
    """ ATMSW class implementing the ATM switch
    """

    def __init__(self, renderer_normal, renderer_select):
        
        AbstractNode.__init__(self, renderer_normal, renderer_select)
        
        # assign a new hostname
        global atm_id
        self.hostname = 'A' + str(atm_id)
        atm_id = atm_id + 1
        self.setCustomToolTip()

        self.config = None
        self.dynagen = globals.GApp.dynagen
        self.a= 'ATMSW ' + self.hostname
        self.d = None
        self.hypervisor = None
        self.running_config = None
        self.atmsw = None
        self.dynagen.update_running_config()

    def __del__(self):
    
        if self.atmsw:
            self.atmsw.delete()
            del self.dynagen.devices[self.hostname]
        self.dynagen.update_running_config()

    def create_config(self):
        """ Creates the configuration of this switch
        """

        self.config = {}
        self.config['ports'] = []
        self.config['mapping'] = {}

    def get_config(self):
        """ Returns the local configuration copy
        """

        return self.config

    def set_config(self, config):
        """ Set a configuration in Dynamips
            config: dict
        """
        
        self.config = config
        
    def set_hypervisor(self,  hypervisor):
        """ Records an hypervisor
            hypervisor: object
        """
    
        self.hypervisor = hypervisor
        self.d = self.hypervisor.host + ':' + str(self.hypervisor.port)

    def getInterfaces(self):
        """ Return all interfaces
        """

        ports = map(int, self.config['ports'])
        ports.sort()
        return (map(str, ports))
        
    def get_dynagen_device(self):
        """ Returns the dynagen device corresponding to this switch
        """
        
        if not self.atmsw:
            self.atmsw = lib.ATMSW(self.hypervisor, name = self.hostname)
            self.dynagen.devices[self.hostname] = self.atmsw
            self.dynagen.update_running_config()
            self.running_config = self.dynagen.running_config[self.d][self.a]
        return (self.atmsw)
        
    def configNode(self):
        """ Node configuration
        """
    
        self.create_config()
        return True
        
    def startNode(self):
        """ Start the node
        """

        connected_interfaces = map(int,  self.getConnectedInterfaceList())
        for (source,  destination) in self.config['mapping'].iteritems():
            match_srcvci = MAPVCI.search(source)
            match_destvci = MAPVCI.search(destination)
            if match_srcvci and match_destvci:
                (srcport,  srcvci,  srcvpi) = match_srcvci.group(1,2,3)
                (destport,  destvci,  destvpi) = match_destvci.group(1,2,3)
            else:
                (srcport,  srcvpi) = source.split(':')
                (destport,  destvpi) = destination.split(':')
                srcvci = destvci = None

            if int(srcport) in connected_interfaces and int(destport) in connected_interfaces:
                if not self.atmsw.connected('a', int(srcport)):
                    if srcvci and destvci:
                        self.atmsw.mapvc(int(srcport), int(srcvpi), int(srcvci), int(destport), int(destvpi),  int(destvci))
                    else:
                        self.atmsw.mapvp(int(srcport), int(srcvpi), int(destport), int(destvpi))
                if not self.atmsw.connected('a', int(destport)):
                    if srcvci and destvci:
                        self.atmsw.mapvc(int(destport), int(destvpi), int(destvci), int(srcport), int(srcvpi),  int(srcvci))
                    else:
                        self.atmsw.mapvp(int(destport), int(destvpi), int(srcport), int(srcvpi))

        self.startupInterfaces()
        globals.GApp.mainWindow.treeWidget_TopologySummary.changeNodeStatus(self.hostname, 'running')

    def mousePressEvent(self, event):
        """ Call when the node is clicked
            event: QtGui.QGraphicsSceneMouseEvent instance
        """

        if globals.addingLinkFlag and globals.currentLinkType != globals.Enum.LinkType.Manual and event.button() == QtCore.Qt.LeftButton:
            connected_ports = self.getConnectedInterfaceList()
            for port in self.config['ports']:
                if not str(port) in connected_ports:
                    self.emit(QtCore.SIGNAL("Add link"), self.id, str(port))
                    return
            QtGui.QMessageBox.critical(globals.GApp.mainWindow, translate("ATMSW", "Connection"),  translate("ATMSW", "No port available"))
            # tell the scene to cancel the link addition by sending a None id and None interface
            self.emit(QtCore.SIGNAL("Add link"), None, None)
        else:
            AbstractNode.mousePressEvent(self, event)
