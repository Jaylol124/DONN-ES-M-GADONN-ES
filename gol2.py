

class GOLEngine:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__world = []
        self.__temp = []
        # construire matrices
        # ...
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
        if not isinstance(width, int) or width < 3 or width > 1000:
            raise ValueError('width must be between 3 and 10000')
        if not isinstance(height, int) or height < 3 or width > 1000:
            raise ValueError('width must be between 3 and 10000')

    def randomize(self, percent=0.5):
        # to do
        pass
        
    def process(self):
        # to do
        pass
    
    
    
def main():
    gol_engine = GOLEngine(12, 8)
    
    gol_engine.randomize()
    
    gol_engine.process()
    
    print(gol_engine.width)
    
    gol_engine.width = 100
    gol_engine.height = 100
    gol_engine.resize('yo', 100)
    gol_engine.process()
        
    

if __name__ == '__main__':
    main()
    

