# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MojaWtyczkaDialog
                                 A QGIS plugin
 Obliczanie różnic wysokości oraz pola powierzchni
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-08
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Piotr 
        email                : piotrzawistowski56@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""



import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

from qgis.core import QgsMessageLog, Qgis, QgsCoordinateReferenceSystem, QgsCoordinateTransform
import numpy as np
from scipy.spatial import Delaunay

from qgis.core import QgsGeometry

from qgis.core import QgsProject, QgsPointXY
from qgis.utils import iface


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wtyczka_pr2_dialog_base.ui'))


def PL002GK(x_00, y_00):
    strefa = int(y_00 / 1000000)
    xgk = x_00 / 0.999923
    ygk = (y_00 - strefa * 1000000 - 500000) / 0.999923
    return xgk, ygk

class MojaWtyczkaDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MojaWtyczkaDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_count.clicked.connect(self.roznica_wys)
        self.pushButton_count2.clicked.connect(self.pole_pow)
        
      
    def roznica_wys(self):
        pkt = self.mMapLayerComboBox.currentLayer().selectedFeatures()
        
        if len(pkt) == 2:
            pkt1 = pkt[0]
            pkt2 = pkt[1]
        elif len(pkt) > 2:
            self.label_dialog_base.setText('wybrano za dużo punktów')
        elif len(pkt) < 2:
            self.label_dialog_base.setText('wybrano za mało punktów')
           
        wys1 = pkt1['H_PLEVRF2007NH']
        wys2 = pkt2['H_PLEVRF2007NH']
                
        height_diff = float(wys2) - float(wys1)
                
        if height_diff > 0:
            height_diff = height_diff 
        elif height_diff < 0:
            height_diff = height_diff * (-1)
           
        height_diff = round(height_diff, 3)    
            
        self.label_dialog_base.setText('przewyższenie jest równe: ' + str(height_diff) + ' m')
        
   

    def pole_pow(self):
        pkt = self.mMapLayerComboBox.currentLayer().selectedFeatures()
        punkty = []
        for i in pkt:
            #x = float(i.attribute('x2000'))
            #y = float(i.attribute('y2000'))
            x = float(i.geometry().asPoint().x())
            y = float(i.geometry().asPoint().y())
            p = QgsPointXY(x, y)
            punkty.append(p)
        if len(pkt)<3:
            self.label_dialog_base2.setText('Wybierz co najmniej 3 punkty')
           
        if len(pkt)>2:
            pole = 0
           
            dlugosc = len(punkty)
            for e in range(dlugosc):
                a = (e + 1) % dlugosc
                pole += (punkty[a].x() + punkty[e].x()) * (punkty[a].y() - punkty[e].y())
            pole /= 2
            pole = abs(pole)
            pole = round(pole, 3)    

            self.label_dialog_base2.setText('pole powierzchni jest równe: ' + str(pole) + ' m^2')
        
            



