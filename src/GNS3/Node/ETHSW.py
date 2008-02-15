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

from GNS3.Node.AbstractNode import AbstractNode
from PyQt4 import QtCore, QtGui
from GNS3.Utils import translate
import GNS3.Dynagen.dynamips_lib as lib
import GNS3.Dynagen.dynagen as dynagen_namespace
import GNS3.Globals as globals 

ethsw_id = 0

class ETHSW(AbstractNode):
    """ ETHSW class implementing the Ethernet switch
    """

    def __init__(self, renderer_normal, renderer_select):
        
        AbstractNode.__init__(self, renderer_normal, renderer_select)
        
        # assign a new hostname
        global ethsw_id
        self.hostname = 'S' + str(ethsw_id)
        ethsw_id = ethsw_id + 1
        self.setCustomToolTip()

        self.config = None
        self.dynagen = globals.GApp.dynagen
        self.e = 'ETHSW ' + self.hostname
        self.d = None
        self.hypervisor = None
        self.running_config = None
        self.ethsw = None
        self.dynagen.update_running_config()

    def __del__(self):
    
        self.delete_ethsw()
        
    def delete_ethsw(self):

        if self.ethsw:
            self.ethsw.delete()
            del self.dynagen.devices[self.hostname]
            self.ethsw = None
        self.dynagen.update_running_config()
    
    def set_hostname(self, hostname):
        """ Set a hostname
        """
        
        self.hostname = hostname
        self.e = 'ETHSW ' + self.hostname
        
    def get_running_config_name(self):
        """ Return node name as stored in the running config
        """
        
        return (self.e)
        
    def create_config(self):
        """ Creates the configuration of this switch
        """

        self.config = {}
        self.config['vlans'] = {}
        self.config['ports'] = {}
        # by default create 8 ports in vlan 1
        self.config['vlans'][1] = []
        for port in range(1, 9):
            self.config['ports'][port] = 'access'
            self.config['vlans'][1].append(port)

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
        """ Returns all interfaces
        """

        ports = map(str, self.config['ports'].keys())
        return (ports) 

    def get_dynagen_device(self):
        """ Returns the dynagen device corresponding to this switch
        """
        
        if not self.ethsw:
            self.ethsw = lib.ETHSW(self.hypervisor, name = self.hostname)
            self.dynagen.devices[self.hostname] = self.ethsw
        if not self.dynagen.running_config[self.d].has_key(self.e):
            self.dynagen.update_running_config()
            self.running_config = self.dynagen.running_config[self.d][self.e]
        return (self.ethsw)

    def set_dynagen_device(self, ethsw):
        """ Set a dynagen device in this node, used for .net import
        """

        self.ethsw = ethsw
        
    def reconfigNode(self, new_hostname):
        """ Used when changing the hostname
        """

        links = self.getEdgeList().copy()
        for link in links:
            globals.GApp.topology.deleteLink(link)
        self.delete_ethsw()
        self.hostname = new_hostname
        self.e = 'ETHSW ' + self.hostname
        if len(links):
            self.get_dynagen_device()
            for link in links:
                globals.GApp.topology.addLink(link.source.id, link.srcIf, link.dest.id, link.destIf)
        
    def configNode(self):
        """ Node configuration
        """

        self.create_config()
        return True
        
    def startNode(self):
        """ Start the node
        """

        connected_interfaces = map(int, self.getConnectedInterfaceList())
        for (vlan, portlist) in self.config['vlans'].iteritems():
            for port in portlist:
                if port in connected_interfaces:
                    (destnode, destinterface)= self.getConnectedNeighbor(str(port))
                    porttype = self.config['ports'][port]
                    if destinterface.lower()[:3] == 'nio':
                        self.dynagen.ethsw_map(self.ethsw, port, porttype + ' ' + str(vlan) + ' ' + destinterface)
                    else:
                        self.dynagen.ethsw_map(self.ethsw, port, porttype + ' ' + str(vlan))

        self.startupInterfaces()
        self.state = 'running'
        globals.GApp.mainWindow.treeWidget_TopologySummary.changeNodeStatus(self.hostname, 'running')

    def mousePressEvent(self, event):
        """ Call when the node is clicked
            event: QtGui.QGraphicsSceneMouseEvent instance
        """

        if globals.addingLinkFlag and globals.currentLinkType != globals.Enum.LinkType.Manual and event.button() == QtCore.Qt.LeftButton:
            connected_ports = self.getConnectedInterfaceList()
            for port in self.config['ports'].keys():
                if not str(port) in connected_ports:
                    self.emit(QtCore.SIGNAL("Add link"), self.id, str(port))
                    return
            QtGui.QMessageBox.critical(globals.GApp.mainWindow, translate("ETHSW", "Connection"),  translate("ETHSW", "No port available"))
            # tell the scene to cancel the link addition by sending a None id and None interface
            self.emit(QtCore.SIGNAL("Add link"), None, None)
        else:
            AbstractNode.mousePressEvent(self, event)
