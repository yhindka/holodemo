#!/usr/bin/env python

class Zone:

    def __init__(self, dimx, dimz, posx, posy, posz, danger):
        self.dimx = dimx
        self.dimz = dimz
        self.posx = posx
        self.posy = posy
        self.posz = posz
        self.danger = danger

class Zones:
    

    def __init__(self):
        self.zones = []

    def getZone(self, index):
        
        zone = self.zones[index]
        return (zone.dimx, zone.dimz, zone.posx, zone.posy, zone.posz, zone.danger)

    def addZone(self, zone):
        
        self.zones.append(zone)

    def removeZone(self, index):
        del self.zones[index]


