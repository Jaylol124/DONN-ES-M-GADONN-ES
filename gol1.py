import random

width = 12
height = 8

world = []
temp = []
for x in range(width):
    world.append([])
    temp.append([])
    for _ in range(height):
        world[x].append(random.randint(0, 1))
        # world[x].append(0 if random.random() <= 0.5 else 1)
        temp[x].append(0)
        
for y in range(height):
    for x in range(width):
        print(world[x][y], end='')
    print()
    
    
for x in range(1, width-1):
    for y in range(1, height-1):
        neighbours = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if i != 0 or j != 0:
                    # neighbours += 1 if world[x+i][y+j] == 1 else 0
                    neighbours += world[x+i][y+j]
        if world[x][y] == 0: # mort
            temp[x][y] = 1 if neighbours == 3 else 0
        else: # vivant
            # temp[x][y] = 1 if neighbours == 2 or neighbours == 3 else 0
            temp[x][y] = 1 if neighbours in (2, 3) else 0
        
        
for y in range(height):
    for x in range(width):
        world[x][y] = temp[x][y]
        
                
print('-' * 40)        
for y in range(height):
    for x in range(width):
        print(world[x][y], end='')
    print()
            
pass