class Human:
    def __init__(self, name=''):
        self.name = name
        self.value = 3
        # convention
        self._speed = 0
        self._protected_value = 0
        self.__private_value = 0 # self.__... => name mangling => _Human__private_value
        
    def f1(self):
        print(f'member function of Class {type(self).__name__} located at {hex(id(self))}.')
        
    def f2():
        print('Static function')
        
    @property
    def speed(self):
        return self._speed
        
    @speed.setter
    def speed(self, value):
        self._speed = max(0, value)
    
        
roger = Human('Roger')

roger.yo = 'cool'

roger.value = 5
roger._protected_value = 10
roger._Human__private_value = 100

roger.f1()
#roger.f2()
Human.f2()


roger._speed = 128
print(roger._speed)
roger.speed = -128
print(roger.speed)

pass        
        