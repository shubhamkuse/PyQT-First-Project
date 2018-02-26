#Version 0.1

#Versions History
#Number     Date            Author      Change
#0.3        Jan 24th,2017   Shubham    Working Version

import os
import sys
import time
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PyQt4 import QtGui,QtCore

from dt import Ui_MainWindow


class demoMainClass(QtGui.QMainWindow,Ui_MainWindow):
    aX1 =  ("0")
    aX2 =  ("0")
    aX3 =  ("0")
    aY1 =  ("0")
    aY2 =  ("0")
    aY3 =  ("0")
    aR1 =  ("0")
    aR2 =  ("0")
    aR3 =  ("0")
       
    def __init__(self,parent=None):
        super(demoMainClass,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("TRIANGULATION")
        self.demoWindowInitialize()
        self.demoFunction()
        
   
    def demoWindowInitialize(self):
        self.X1.insert(self.aX1)
        self.X2.insert(self.aX2)
        self.X3.insert(self.aX3)
        self.Y1.insert(self.aY1)
        self.Y2.insert(self.aY2)
        self.Y3.insert(self.aY3)
        self.R1.insert(self.aR1)
        self.R2.insert(self.aR2)
        self.R3.insert(self.aR3)
        self.Generate.clicked.connect(lambda: self.demoFunction())
        self.Generate.clicked.connect(lambda: self.demoPlot())
        
    def demoFunction(self):
        global x1
        global x2
        global x3
        global y1
        global y2
        global y3
        global r1
        global r2
        global r3
        global x_centroid
        global y_centroid
        x1=float(self.X1.text())
        x2=float(self.X2.text())
        x3=float(self.X3.text())
        y1=float(self.Y1.text())
        y2=float(self.Y2.text())
        y3=float(self.Y3.text())
        r1=float(self.R1.text())
        r2=float(self.R2.text())
        r3=float(self.R3.text())

        
        if ( x1==0 and x2==0 and x3==0 and y1==0 and y2==0 and y3==0 and r1==0 and r2==0 and r3==0 ):
            self.Generate_show.setText(" ")
        else:
                
            def d(xd1,yd1,xd2,yd2):
                dist = ((xd2-xd1)**2 + (yd2-yd1)**2)
                return (math.sqrt(dist))

            def z(rz1,rz2,d):
                zeta = (((rz1+rz2)**2 - (d)**2)*((d)**2 - (rz1-rz2)**2))
                return (math.sqrt(zeta))

            def xc(xo1,xo2,yo1,yo2,ro1,ro2,do,zo):
                xc1 = (((xo2+xo1)/2))+((xo2-xo1)*((ro1)**2-(ro2)**2)/(2*(do)**2))+(((yo2-yo1) * zo / (2*do**2) ))
                xc2 = (((xo2+xo1)/2))+((xo2-xo1)*((ro1)**2-(ro2)**2)/(2*(do)**2))-(((yo2-yo1) * zo / (2*do**2) ))
                yc1 = (((yo2+yo1)/2))+((yo2-yo1)*((ro1)**2-(ro2)**2)/(2*(do)**2))-(((xo2-xo1) * zo / (2*do**2) ))
                yc2 = (((yo2+yo1)/2))+((yo2-yo1)*((ro1)**2-(ro2)**2)/(2*(do)**2))+(((xo2-xo1) * zo / (2*do**2) ))
                return [xc1,xc2,yc1,yc2]
            
            if (r1 - r2)**2 < (x1 - x2)**2 + (y1 -y2)**2 < (r1+r2)**2 and (r2 - r3)**2 < (x2 - x3)**2 + (y2 - y3)**2 < (r2+r3)**2 and (r3 - r1)**2 <= (x3 - x1)**2 + (y3 - y1)**2 <= (r3+r1)**2 :
                d1 = d(x1,y1,x2,y2)
                z1 = z(r1,r2,d1)
                xcs1 = xc (x1,x2,y1,y2,r1,r2,d1,z1) 
                vx1 = xcs1 [0]
                vx2 = xcs1 [1]
                vy1 = xcs1 [2]
                vy2 = xcs1 [3]
                d2 = d(x2,y2,x3,y3)
                z2 = z(r2,r3,d2)
                xcs2 = xc (x2,x3,y2,y3,r2,r3,d2,z2) 
                vx3 = xcs2 [0]
                vx4 = xcs2 [1]
                vy3 = xcs2 [2]
                vy4 = xcs2 [3]
                d3 = d(x1,y1,x3,y3)
                z3 = z(r1,r3,d3)
                xcs3 = xc (x1,x3,y1,y3,r1,r3,d3,z3) 
                vx5 = xcs3 [0]
                vx6 = xcs3 [1]
                vy5 = xcs3 [2]
                vy6 = xcs3 [3]
                x_centroid = (vx1+vx2+vx3+vx4+vx5+vx6)/6
                y_centroid = (vy1+vy2+vy3+vy4+vy5+vy6)/6
                centroid = str(x_centroid)+' , '+  str(y_centroid)
                self.Generate_show.setText(centroid)
                
                
            elif ((r1 - r2)**2 < (x1 - x2)**2 + (y1 -y2)**2 < (r1+r2)**2 and (r2 - r3)**2 < (x2 - x3)**2 + (y2 - y3)**2 < (r2+r3)**2 ) or ((r1 - r2)**2 < (x1 - x2)**2 + (y1 -y2)**2 < (r1+r2)**2 and(r3 - r1)**2 < (x3 - x1)**2 + (y3 - y1)**2 < (r3+r1)**2 ) or ((r2 - r3)**2 < (x2 - x3)**2 + (y2 - y3)**2 < (r2+r3)**2 and (r3 - r1)**2 < (x3 - x1)**2 + (y3 - y1)**2 < (r3+r1)**2) :
                if ((r1 - r2)**2 < (x1 - x2)**2 + (y1 -y2)**2 < (r1+r2)**2 and (r2 - r3)**2 < (x2 - x3)**2 + (y2 - y3)**2 < (r2+r3)**2 ):
                    d1 = d(x1,y1,x2,y2)
                    z1 = z(r1,r2,d1)
                    xcs1 = xc (x1,x2,y1,y2,r1,r2,d1,z1) 
                    vx1 = xcs1 [0]
                    vx2 = xcs1 [1]
                    vy1 = xcs1 [2]
                    vy2 = xcs1 [3]
                    d2 = d(x2,y2,x3,y3)
                    z2 = z(r2,r3,d2)
                    xcs2 = xc (x2,x3,y2,y3,r2,r3,d2,z2) 
                    vx3 = xcs2 [0]
                    vx4 = xcs2 [1]
                    vy3 = xcs2 [2]
                    vy4 = xcs2 [3]
                    x_centroid = (vx1+vx2+vx3+vx4+x2)/5
                    y_centroid = (vy1+vy2+vy3+vy4+y2)/5
                    x_centroid = (vx1+vx2+vx3+vx4+vx5+vx6)/6
                    y_centroid = (vy1+vy2+vy3+vy4+vy5+vy6)/6
                    centroid = str(x_centroid)+' , '+  str(y_centroid)
                    self.Generate_show.setText(centroid)
                    
                if ((r1 - r2)**2 < (x1 - x2)**2 + (y1 -y2)**2 < (r1+r2)**2 and (r3 - r1)**2 < (x3 - x1)**2 + (y3 - y1)**2 < (r3+r1)**2 ):
                    d1 = d(x1,y1,x2,y2)
                    z1 = z(r1,r2,d1)
                    xcs1 = xc (x1,x2,y1,y2,r1,r2,d1,z1) 
                    vx1 = xcs1 [0]
                    vx2 = xcs1 [1]
                    vy1 = xcs1 [2]
                    vy2 = xcs1 [3]
                    d3 = d(x1,y1,x3,y3)
                    z3 = z(r1,r3,d3)
                    xcs3 = xc (x1,x3,y1,y3,r1,r3,d3,z3)
                    vx3 = xcs3 [0]
                    vx4 = xcs3 [1]
                    vy3 = xcs3 [2]
                    vy4 = xcs3 [3]
                    x_centroid = (vx1+vx2+vx3+vx4+x1)/5
                    y_centroid = (vy1+vy2+vy3+vy4+y1)/5
                    centroid = str(x_centroid)+' , '+  str(y_centroid)
                    self.Generate_show.setText(centroid)
                    
                if ((r2 - r3)**2 < (x2 - x3)**2 + (y2 - y3)**2 < (r2+r3)**2 and (r3 - r1)**2 < (x3 - x1)**2 + (y3 - y1)**2 < (r3+r1)**2) :
                    d2 = d(x2,y2,x3,y3)
                    z2 = z(r2,r3,d2)
                    xcs2 = xc (x2,x3,y2,y3,r2,r3,d2,z2)
                    vx1 = xcs2 [0]
                    vx2 = xcs2 [1]
                    vy1 = xcs2 [2]
                    vy2 = xcs2 [3]
                    d3 = d(x1,y1,x3,y3)
                    z3 = z(r1,r3,d3)
                    xcs3 = xc (x1,x3,y1,y3,r1,r3,d3,z3) 
                    vx3 = xcs3 [0]
                    vx4 = xcs3 [1]
                    vy3 = xcs3 [2]
                    vy4 = xcs3 [3]
                    x_centroid = (vx1+vx2+vx3+vx4+x3)/5
                    y_centroid = (vy1+vy2+vy3+vy4+y3)/5
                    centroid = str(x_centroid)+' , '+  str(y_centroid)
                    self.Generate_show.setText(centroid) 
                    
            elif (r1 - r2)**2 < (x1 - x2)**2 + (y1 -y2)**2 < (r1+r2)**2 or (r2 - r3)**2 < (x2 - x3)**2 + (y2 - y3)**2 < (r2+r3)**2 or (r3 - r1)**2 <= (x3 - x1)**2 + (y3 - y1)**2 <= (r3+r1)**2 :
                if (r1 - r2)**2 < (x1 - x2)**2 + (y1 -y2)**2 < (r1+r2)**2 :
                    d1 = d(x1,y1,x2,y2)
                    z1 = z(r1,r2,d1)
                    xcs1 = xc (x1,x2,y1,y2,r1,r2,d1,z1)
                    vx1 = xcs1 [0]
                    vx2 = xcs1 [1]
                    vy1 = xcs1 [2]
                    vy2 = xcs1 [3]
                    x_centroid = (vx1+vx2+x3)/3
                    y_centroid = (vy1+vy2+y3)/3
                    centroid = str(x_centroid)+' , '+  str(y_centroid)
                    self.Generate_show.setText(centroid)
                    
                if (r2 - r3)**2 < (x2 - x3)**2 + (y2 - y3)**2 < (r2+r3)**2 :
                     d2 = d(x2,y2,x3,y3)
                     z2 = z(r2,r3,d2)
                     xcs2 = xc (x2,x3,y2,y3,r2,r3,d2,z2)
                     vx1 = xcs2 [0]
                     vx2 = xcs2 [1]
                     vy1 = xcs2 [2]
                     vy2 = xcs2 [3]
                     x_centroid = (vx1+vx2+x1)/3
                     y_centroid = (vy1+vy2+y1)/3
                     centroid = str(x_centroid)+' , '+  str(y_centroid)
                     self.Generate_show.setText(centroid)
                     
                if (r3 - r1)**2 <= (x3 - x1)**2 + (y3 - y1)**2 <= (r3+r1)**2 :
                    d3 = d(x1,y1,x3,y3)
                    z3 = z(r1,r3,d3)
                    xcs3 = xc (x1,x3,y1,y3,r1,r3,d3,z3)
                    vx1 = xcs3 [0]
                    vx2 = xcs3 [1]
                    vy1 = xcs3 [2]
                    vy2 = xcs3 [3]
                    x_centroid = (vx1+vx2+x2)/3
                    y_centroid = (vy1+vy2+y2)/3
                    centroid = str(x_centroid)+' , '+  str(y_centroid)
                    self.Generate_show.setText(centroid)
            
            else:
            
                x_centroid = (x1+x2+x3)/3
                y_centroid = (y1+y2+y3)/3
                centroid = str(x_centroid)+' , '+  str(y_centroid)
                self.Generate_show.setText(centroid)
                
    def demoPlot(self):
        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111, aspect='equal')
        ax2.add_patch(
            patches.Circle(
                (x1, y1),
                r1,
                fill=False
            )
        )

        ax2.add_patch(
            patches.Circle(
                (x2, y2),
                r2,
                fill=False
            )
        )

        ax2.add_patch(
            patches.Circle(
                (x3, y3),
                r3,
                fill=False
            )
        )
        plt.plot([x_centroid], [y_centroid], 'ro')
        plt.show()
            
if __name__ == "__main__":
   
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = demoMainClass()
    ui.show()
    sys.exit(app.exec_())

