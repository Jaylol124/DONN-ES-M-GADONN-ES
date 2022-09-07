from ast import Pass
from random import random, randint
from turtle import heading

            
class GOLEngine:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__world = None
        self.__temp = None
        #contruire matrice
        
        self.resize(10,10)
        #self.randomize()
       
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
        if not isinstance(width, int) or width < 3 or width > 1000:
            raise ValueError('width must be between 3 and 10000')
        if not isinstance(height, int) or height < 3 or width > 1000:
            raise ValueError('width must be between 3 and 10000')
        else:
            self.__width = width
            self.__height = height
            self.__world = []
            self.__temp = []

        for x in range(width):
            self.__world.append([])
            self.__temp.append([])
            for _ in range(height):
                self.__world[x].append(randint(0, 1))
                # world[x].append(0 if random.random() <= 0.5 else 1)
                self.__temp[x].append(0)

        for y in range(self.__height):
            for x in range(self.__width):
                self.__temp[x][y] = self.__world[x][y]

       
    def randomize(self, percent=0.5):

        for x in range(self.__width):
            for _ in range(self.__height):
                self.__world[x] == randint(0, 1)
                # world[x].append(0 if random.random() <= 0.5 else 1)
                self.__temp[x].append(0)

        for y in range(self.__height):
            for x in range(self.__width):
                self.__temp[x][y] = self.__world[x][y]


        
    def process(self):
        for x in range(1, self.__width - 1):
            for y in range(1, self.__height - 1):
                neighbours = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i != 0 or j != 0:
                            # neighbours += 1 if world[x+i][y+j] == 1 else 0
                            neighbours += self.__world[x + i][y + j]
                if self.__world[x][y] == 0:  # mort
                    self.__temp[x][y] = 1 if neighbours == 3 else 0
                else:  # vivant
                    # temp[x][y] = 1 if neighbours == 2 or neighbours == 3 else 0
                    self.__temp[x][y] = 1 if neighbours in (2, 3) else 0

        #for y in range(self.__height): #methode pour garder le contour
        #    for x in range(self.__width):
        #        if y == 0:
        #            self.__temp[x][y] = self.__world[x][y]
        #        if self.__height - 1 > y > 0:
        #            self.__temp[0][y] = self.__world[0][y]
        #            self.__temp[self.__width - 1][y] = self.__world[self.__width - 1][y]
        #        if y == self.__height:
        #            self.__temp[x][y] = self.__world[x][y]


        for y in range(self.__height):
            for x in range(self.__width):
                self.__world[x][y] = self.__temp[x][y]



def main():
    gol_engine = GOLEngine(10,10)

    for i in gol_engine._GOLEngine__world:
        print(i)

    gol_engine.randomize()

    print("\n")

    gol_engine.process()

    for i in gol_engine._GOLEngine__world:
        print(i)

    
if __name__ == '__main__':
    main()
