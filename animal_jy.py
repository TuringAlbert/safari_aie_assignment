

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
        
    def move(self, direction="right"):
        print(f'moving to {direction}. <<<NOT IMPLEMENTED YET>>>')
        self.x += 1
        
    def breed(self, x, y):
         return Animal(x, y)

class Zebra(Animal):
    def move(self, occupancy_grid):
        self.y += 1
        print('<<< NOT IMPLEMENTED >>>')
    def breed(self, x, y):
        print('<<< NOT IMPLEMENTED >>>>>')


class Lion(Animal):
    def move(self, occupancy_grid):
        self.x += 1
        print('<<< NOT IMPLEMENTED >>>')
