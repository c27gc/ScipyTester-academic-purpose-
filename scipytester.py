#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
from PyQt4 import QtGui
from PyQt4 import QtCore
import numpy as np
import sympy
from sympy.parsing.sympy_parser import standard_transformations
from sympy.parsing.sympy_parser import implicit_multiplication_application
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

transformations = (standard_transformations + (implicit_multiplication_application,))

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Scipy Tester')
        self.grid = QtGui.QGridLayout()
        self.setStyleSheet("background: qlineargradient( x1:1 y1:0, x2:1 y2:1, stop:0 white, stop:1 #193737);}")

        self.boton = QtGui.QPushButton('Ecuaciones Diferenciales', self)
        self.boton.setStyleSheet("QPushButton {background-color:#193737;\
        font-size: 20px; font-family:'Arial'; font-variant:small-caps;\
        font-weight:bold; color:'white'; border-radius:20px;}" "QPushButton:hover \
        {background-color:'white'; color:#193737;}"\
        "QPushButton:focus {outline: 0;}")
        self.connect(self.boton, QtCore.SIGNAL('clicked()'),self.ecuaciones)
        self.boton.setMinimumWidth(250)
        self.boton.setMaximumWidth(250)
        self.boton.setMinimumHeight(120)
        self.boton.setMaximumHeight(120)
        self.boton.setDefault(False)
        self.grid.addWidget(self.boton,2,1)

        self.boton1 = QtGui.QPushButton('Ajustes no Lineales', self)
        self.boton1.setStyleSheet("QPushButton {background-color:#193737;\
        font-size: 20px; font-family:'Arial'; font-variant:small-caps;\
        font-weight:bold; color:'white'; border-radius:20px;}" "QPushButton:hover \
        {background-color:'white'; color:#193737;}"\
        "QPushButton:focus {outline: 0;}")
        self.connect(self.boton1, QtCore.SIGNAL('clicked()'),self.fitC)
        self.boton1.setMinimumWidth(250)
        self.boton1.setMaximumWidth(250)
        self.boton1.setMinimumHeight(120)
        self.boton1.setMaximumHeight(120)

        self.boton2 = QtGui.QPushButton('Pseudo Inversa', self)
        self.boton2.setStyleSheet("QPushButton {background-color:#193737;\
        font-size: 20px; font-family:'Arial'; font-variant:small-caps;\
        font-weight:bold; color:'white'; border-radius:20px;}" "QPushButton:hover \
        {background-color:'white'; color:#193737;}"\
        "QPushButton:focus {outline: 0;}")
        self.connect(self.boton2, QtCore.SIGNAL('clicked()'),self.pseudo)
        self.boton2.setMinimumWidth(250)
        self.boton2.setMaximumWidth(250)
        self.boton2.setMinimumHeight(120)
        self.boton2.setMaximumHeight(120)
        self.grid.addWidget(self.boton2,2,5)

        self.labelAux = QtGui.QLabel(" ")
        self.labelAux.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.grid.addWidget(self.labelAux,2,0)


        self.labelAux3 = QtGui.QLabel(" ")
        self.labelAux3.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.grid.addWidget(self.labelAux3,2,6)

        self.labelArriba = QtGui.QLabel("Scipy Tester")
        self.labelArriba.setStyleSheet("border; 1px solid red; color:#193737;" "background-color:rgba(0, 0, 0, 0);"
        "font-size: 95px;" "font-family:'Arial';" "font-variant:small-caps;" "font-weight:bold;")
        self.grid.addWidget(self.labelArriba,1,3)

        self.labelAbajo = QtGui.QLabel(" ")
        self.labelAbajo.setMaximumHeight(250)
        self.labelAbajo.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.grid.addWidget(self.labelAbajo,3,3)

        self.botonA = QtGui.QPushButton('Acerca de', self)
        self.botonA.setStyleSheet("QPushButton {background-color:white;\
        font-size: 20px; font-family:'Arial'; font-variant:small-caps;\
        font-weight:bold; color:#193737; border-radius:20px;}" "QPushButton:hover \
        {background-color:#193737; color:white;}"\
        "QPushButton:focus {outline: 0;}")
        self.connect(self.botonA, QtCore.SIGNAL('clicked()'),self.acerca)

        self.botonB = QtGui.QPushButton('Ayuda', self)
        self.botonB.setStyleSheet("QPushButton {background-color:white;\
        font-size: 20px; font-family:'Arial'; font-variant:small-caps;\
        font-weight:bold; color:#193737; border-radius:20px;}" "QPushButton:hover \
        {background-color:#193737; color:white;}"\
        "QPushButton:focus {outline: 0;}")
        self.connect(self.botonB, QtCore.SIGNAL('clicked()'),self.ayudap)


        hBL=QtGui.QHBoxLayout()
        hBL.addWidget(self.botonA)
        hBL.addWidget(self.botonB)
        self.grid.addLayout(hBL,4,3)

        Hbox=QtGui.QHBoxLayout()
        Hbox.addWidget(self.boton1)
        self.grid.addLayout(Hbox, 2,3)

        self.setLayout(self.grid)
        self.showMaximized()

    def ayudap(self):
        self.ventana2 = Ayuda().exec_()

    def pseudo(self):
        self.ven1 = PseudoInversa()
        self.ven1.show()

    def ecuaciones(self):
        self.ven2 = Ecuaciones()
        self.ven2.show()

    def fitC(self):
        self.ven3 = Fit()
        self.ven3.show()

    def acerca(self):
        self.ventana = Acercade().exec_()

class Acercade(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        contenedor = QtGui.QVBoxLayout()
        self.setLayout(contenedor)
        self.setWindowTitle('Acerca de')
        cadena1 = "Programa creado por: Carlos E. González C."
        cadena2 = "Ingenieria del Software Maestría"
        cadena3 = "Ingeniería Electrica"
        cadena4 = "Universidad Central de Venezuela."
        Lbl = QtGui.QLabel("{}\n{}\n{}\n{}".format(cadena1.ljust(0, ' '),cadena2.ljust(0, ' '),cadena3.ljust(0, ' '),cadena4.ljust(0, ' ')))
        contenedor.addWidget(Lbl)

class Ayuda(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        contenedor = QtGui.QVBoxLayout()
        self.setLayout(contenedor)
        self.setWindowTitle('Acerca de')
        cadena1 = "Este programa está  diseñado con el fin de mostrar"
        cadena2 = "las capacidades de Numpy, un proposito es meramente"
        cadena3 = "academico. En ningun momento busca ser una herramienta"
        cadena4 = "de cálculo profesional."
        Lbl = QtGui.QLabel("{}\n{}\n{}\n{}".format(cadena1.ljust(0, ' '),cadena2.ljust(0, ' '),cadena3.ljust(0, ' '),cadena4.ljust(0, ' ')))
        contenedor.addWidget(Lbl)

class AyudaGen(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        contenedor = QtGui.QVBoxLayout()
        self.setLayout(contenedor)
        self.setWindowTitle('Acerca de')
        cadena1 = "Para el cálculo de la pseudo inversa es necesario definir"
        cadena2 = "una matriz, en dicha matriz los elementos de una fila se"
        cadena3 = "separan por espacios y las filas por el caracter ;"
        cadena4 = "Ejemplo, la matriz \n[3 4 -1]\n[0 3 1]\n[1 0 1]\n es definida de la siguiente forma: \n 3 4 -1 ; 0 3 1 ; 1 0 1"
        Lbl = QtGui.QLabel("{}\n{}\n{}\n{}".format(cadena1.ljust(0, ' '),cadena2.ljust(0, ' '),cadena3.ljust(0, ' '),cadena4.ljust(0, ' ')))
        contenedor.addWidget(Lbl)

class AyudaGen2(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        contenedor = QtGui.QVBoxLayout()
        self.setLayout(contenedor)
        self.setWindowTitle('Acerca de')
        cadena1 = "Para la resolución de una ecuación diferencial de primer"
        cadena2 = "orden, es necesario definir la misma. La ecuación diferencial"
        cadena3 = "debe ser ordenada en el siguiente formato"
        cadena4 = "y' = x+3y \nPara la resolución del ejemplo anterior mediante Numpy Tester,\nes necesario introducir x+3y en la barra de texto."
        Lbl = QtGui.QLabel("{}\n{}\n{}\n{}".format(cadena1.ljust(0, ' '),cadena2.ljust(0, ' '),cadena3.ljust(0, ' '),cadena4.ljust(0, ' ')))
        contenedor.addWidget(Lbl)

class AyudaGen3(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        contenedor = QtGui.QVBoxLayout()
        self.setLayout(contenedor)
        self.setWindowTitle('Acerca de')
        cadena1 = "Para el ajuste de una función no lineal, es necesario introducir"
        cadena2 = "dicha función en el siguiente formato: f(x,a,b,c) donde:\n a,b y c son los parámetros a ajustar\nx es la variable independiente.\n"
        cadena3 = "De ser necesario la utilización de funciones predefinidas, estas\nse deben introducir en el formato de numpy, ejemplo\n"
        cadena4 = "f(x,a,b,c)=a*np.exp(b*c*x)\nPara la resolución del ejemplo anterior mediante Numpy Tester,\nes necesario introducir a*np.exp(b*c*x) en la barra de texto.\nEl sistema genera una lista de datos con los cuales se realizará el ajuste."
        Lbl = QtGui.QLabel("{}\n{}\n{}\n{}".format(cadena1.ljust(0, ' '),cadena2.ljust(0, ' '),cadena3.ljust(0, ' '),cadena4.ljust(0, ' ')))
        contenedor.addWidget(Lbl)


class PseudoInversa(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Pseudo Inversa Monroe-Penrose')
        self.grid = QtGui.QGridLayout()
        self.setMinimumWidth(500)
        self.setMaximumWidth(500)
        self.setMinimumHeight(300)
        self.setMaximumHeight(300)

        dfm="Defina la Matriz"
        self.label2 = QtGui.QLabel(dfm.center(75))
        self.label2.setStyleSheet("background-color:white;"
        "font-size: 20px;" "font-family:'Arial';" "font-variant:small-caps;"
        "font-weight:bold;" "background-color:rgba(0, 0, 0, 0);")
        self.grid.addWidget(self.label2,1,1)

        self.botonB3 = QtGui.QPushButton('Invertir', self)
        self.botonB3.setMaximumHeight(30)
        self.connect(self.botonB3, QtCore.SIGNAL('clicked()'),self.inverR)
        self.grid.addWidget(self.botonB3,3,1)

        dfm="Status: "
        self.label2 = QtGui.QLabel(dfm)
        self.label2.setStyleSheet("background-color:white;"
        "font-size: 20px;" "font-family:'Arial';" "font-variant:small-caps;"
        "font-weight:bold;" "background-color:rgba(0, 0, 0, 0);" "borde:1px solid red;")
        self.grid.addWidget(self.label2,4,1)


        self.label211 = QtGui.QTextEdit(" ")
        self.label211.setMinimumWidth(400)
        self.label211.setMinimumHeight(100)
        #self.label211.setMaximumWidth(100)
        #self.label211.setMaximumHeight(100)
        self.grid.addWidget(self.label211,5,1)

        self.botonB = QtGui.QPushButton('Ayuda', self)
        self.botonB.setMaximumHeight(30)
        self.connect(self.botonB, QtCore.SIGNAL('clicked()'),self.ayudapsi)
        self.grid.addWidget(self.botonB,6,1)

        self.tex = QtGui.QLineEdit()
        self.tex.setMaximumWidth(500)
        self.tex.setMaximumHeight(100)
        self.grid.addWidget(self.tex,2,1)

        self.setLayout(self.grid)

    def inverR(self):
        try:
            k=self.tex.text()
            A=np.matrix(k)
            g=type(A)
            strr="La matriz posee inversa:\n"
            self.label211.setText(strr + str(np.linalg.inv(A)))
        except np.linalg.linalg.LinAlgError:
            sttr="La matriz es sigular con pseudo inversa:\n"
            self.label211.setText(sttr + str(np.linalg.pinv(A)))

    def ayudapsi(self):
        self.ventana = AyudaGen().exec_()

class Ecuaciones(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Ecuaciones diferenciales 1er Orden')
        self.grid = QtGui.QGridLayout()
        self.setMinimumWidth(500)
        self.setMaximumWidth(500)
        self.setMinimumHeight(300)
        self.setMaximumHeight(300)

        dfm="Defina la EDO de 1er Orden"
        self.label2 = QtGui.QLabel(dfm.center(65))
        self.label2.setStyleSheet("background-color:white;"
        "font-size: 20px;" "font-family:'Arial';" "font-variant:small-caps;"
        "font-weight:bold;" "background-color:rgba(0, 0, 0, 0);")
        self.grid.addWidget(self.label2,1,2)

        self.botonB3 = QtGui.QPushButton('Cargar', self)
        self.botonB3.setMaximumHeight(30)
        self.connect(self.botonB3, QtCore.SIGNAL('clicked()'),self.solR)
        self.grid.addWidget(self.botonB3,3,2)

        dfm="Status: "
        self.label2 = QtGui.QLabel(dfm)
        self.label2.setStyleSheet("background-color:white;"
        "font-size: 20px;" "font-family:'Arial';" "font-variant:small-caps;"
        "font-weight:bold;" "background-color:rgba(0, 0, 0, 0);" "borde:1px solid red;")
        self.grid.addWidget(self.label2,4,2)


        self.label211 = QtGui.QTextEdit(" ")
        self.label211.setMinimumWidth(400)
        self.label211.setMinimumHeight(100)
        self.grid.addWidget(self.label211,5,2)


        self.botonB = QtGui.QPushButton('Ayuda', self)
        self.botonB.setMaximumHeight(30)
        self.connect(self.botonB, QtCore.SIGNAL('clicked()'),self.ayudapsi2)
        self.grid.addWidget(self.botonB,6,2)

        self.tex = QtGui.QLineEdit()
        self.tex.setMaximumWidth(500)
        self.tex.setMaximumHeight(100)
        self.grid.addWidget(self.tex,2,2)
        self.label22 = QtGui.QLabel("y' = ")
        self.grid.addWidget(self.label22,2,1)

        self.setLayout(self.grid)

    def ayudapsi2(self):
        self.ventana = AyudaGen2().exec_()


    def solR(self):
        x = sympy.Symbol('x')
        y = sympy.Function('y')
        k=self.tex.text()
        try:
            k=self.reac(k)
            f=parse_expr(k, transformations=transformations)
            w=sympy.dsolve(y(x).diff(x) - f)
            self.label211.setText('Solución:\n' + str(w))
        except TypeError:
            self.label211.setText("Error, revisar sección de ayuda.")


    def reac(self,A1):
        K=True
        p=0
        B=A1
        print(B)
        count = 0
        y=0
        while(K):
            A=B[p:]
            y=len(B[0:p])

            n=A.find('y')
            if n==-1:
                break

            B=B[0:p]+A[0:n+1]+'(x)'+A[n+1:]
            p=n+1+y
            count = count +1
            if count > 10:
                print('secorto')
                break
        return B


class Fit(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Ajuste no lineal')
        self.grid = QtGui.QGridLayout()
        self.setMinimumWidth(500)
        self.setMaximumWidth(500)
        self.setMinimumHeight(300)
        self.setMaximumHeight(300)

        dfm="Defina Funcion Objetivo"
        self.label2 = QtGui.QLabel(dfm.center(65))
        self.label2.setStyleSheet("background-color:white;"
        "font-size: 20px;" "font-family:'Arial';" "font-variant:small-caps;"
        "font-weight:bold;" "background-color:rgba(0, 0, 0, 0);")
        self.grid.addWidget(self.label2,1,1)

        self.botonB3 = QtGui.QPushButton('Solucionar', self)
        self.botonB3.setMaximumHeight(30)
        self.connect(self.botonB3, QtCore.SIGNAL('clicked()'),self.fitR)
        self.grid.addWidget(self.botonB3,3,1)

        dfm="Status: "
        self.label2 = QtGui.QLabel(dfm)
        self.label2.setStyleSheet("background-color:white;"
        "font-size: 20px;" "font-family:'Arial';" "font-variant:small-caps;"
        "font-weight:bold;" "background-color:rgba(0, 0, 0, 0);" "borde:1px solid red;")
        self.grid.addWidget(self.label2,4,1)


        self.label211 = QtGui.QTextEdit(" ")
        self.label211.setMinimumWidth(400)
        self.label211.setMinimumHeight(100)
        self.grid.addWidget(self.label211,5,1)

        self.botonB = QtGui.QPushButton('Ayuda', self)
        self.botonB.setMaximumHeight(30)
        self.connect(self.botonB, QtCore.SIGNAL('clicked()'),self.ayudapsi3)
        self.grid.addWidget(self.botonB,6,1)

        self.tex = QtGui.QLineEdit()
        self.tex.setMaximumWidth(500)
        self.tex.setMaximumHeight(100)
        self.grid.addWidget(self.tex,2,1)

        self.setLayout(self.grid)

    def ayudapsi3(self):
        self.ventana = AyudaGen3().exec_()

    def fitR(self):
        self.k=self.tex.text()
        xdata = np.linspace(0, 4, 50)
        y = self.fgeneric(xdata, 2.5, 1.3, 0.5)
        np.random.seed(1551)
        y_noise = 0.2 * np.random.normal(size=xdata.size)
        ydata = y + y_noise
        plt.plot(xdata, ydata, 'b-', label='data')
        popt, pcov = curve_fit(self.fgeneric, xdata, ydata)
        self.label211.setText('Valores reales:\n' + '[2.5 1.3 0.5]'+'\n'+'Ajuste:\n' + str(popt))

        plt.plot(xdata, self.fgeneric(xdata, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    def fgeneric(self,x,a,b,c):
        y=eval(self.k)
        return y

app = QtGui.QApplication(sys.argv)
qb = MainWindow()
qb.show()
sys.exit(app.exec_())
