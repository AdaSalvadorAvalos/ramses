from util import *
import numpy as np

class Euclideo:
    def __init__(self,ficMod=None,ficLisUni=None):
        if ficMod and ficLisUni or not ficLisUni and not ficMod:
            raise ValueError("leete las instrucciones")
        if ficMod:
            self.leeMod(ficMod)
        else :
            self.unidades = leeLis(ficLisUni)
            self.meduni={}
    
    def escMod(self,ficMod):
        with open(ficMod, 'wb') as fpMod:
            np.save(fpMod, self.meduni)

    def leeMod(self, ficMod):
        with open(ficMod,'rb') as fpMod:
            self.meduni = np.load(fpMod)
            self.unidades = self.meduni.keys()

    def initEnt(self):
        self.sumPrm = {unidad: 0 for unidad in self.unidades}
        self.numSen = {unidad: 0 for unidad in self.unidades}

    def __add__(self, mod, señal):
        self.sumPrm[mod] += señal
        self.numSen[mod] += 1

    def recaMod(self):
        for unidad in self.unidades:
            self.meduni[unidad] = self.sumPrm[unidad] / self.numSen[unidad]
    
    def initEval(self):
        self.sumPrm_2 = {unidad: 0 for unidad in self.unidades}
        self.numSen = {unidad: 0 for unidad in self.unidades}

    def addEval(self, mod, señal):
        self.sumPrm_2[mod] += señal ** 2
        self.numSen[mod] += 1

    def recaEval(self):
        distancia_2 = 0
        totSen = 0
        for unidad in self.unidades:
            distancia_2 += self.numSen[unidad] * (self.sumPrm_2[unidad] / self.numSen[unidad] - self.meduni[unidad])
            totSen += self.numSen[unidad]

        self.distancia = (np.sum(distancia_2) / totSen) ** 0.5

    def printEval(self):
        print(f'{self.distancia = :.2f}')