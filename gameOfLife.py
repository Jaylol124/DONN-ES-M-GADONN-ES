from ast import Pass
from random import random
from turtle import heading


class Matrice:
    def __init__(self, hauteur, largeur):
        self.__hauteur = 10
        self.__largeur = 10
        self.intialisation()
        
    def intialisation(self):
        for i in range(self.hauteur): #
            ligne = []
            for j in range(self.largeur):
                if i >= 1 and i<= 8 and j >= 1 and j <= 8:
                    x = random()
                    if x < 0.5:
                        x = 0
                    if x > 0.5:
                        x = 1
                    ligne.append(x)  # append veut dire ajoute
                else:
                    ligne.append(0)  # append veut dire ajoute
                        
            self.matrice.append(ligne)
    

m = Matrice()


for i in m.matrice:
            print(i)
            
class GOLEngine:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__world = []
        self.__temp = []
        #contruire patrice
        
        self.randomize()
       
       
    @property
    def width(self):
        return self.__width   
    
    @width.setter
    def width(self, value):
        pass
    
    @property
    def height(self):
        return self.__height  
    
    @height.setter
    def height(self, value):
        pass
    
    def resize(self, width, height):
        width = max(3, width
                    )
       
    def randomize(self, percent=0.5):
        #to do
        pass   
        
    def process(self):
        #to do
        pass
    

def main():
    gol_engine = GOLEngine(12,8)
    
    gol_engine.randomize()
    
    gol_engine.process()
    
if __name__ == '__main__':
    main()
