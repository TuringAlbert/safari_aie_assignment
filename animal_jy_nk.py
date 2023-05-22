
import random
from utils import print_TODO


class Animal:
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.age = 0
        # self.hp = 3 # 동물의 생명력
        
    def move_to(self, grid, target) -> bool:
        ''' target can be ., L, or Z
        returns True if moved
        '''
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            grid[self.y][self.x] = Empty(self.y, self.x)
            chosen_neighbor = random.choice(neighbors)
            self.y, self.x = chosen_neighbor
            grid[self.y][self.x] = self
            return True
        else:
            return False
        
    def breed(self, y, x):
         print(f'breed for {y}, {x}. <<<NOT IMPLEMENTED YET>>>')
     
    def get_neighbors(self, grid, target):
        '''target can be ., L, or Z
        returns a list of coordinates
        '''
        world_height = len(grid)
        world_width = len(grid[0])
        x, y = self.x, self.y
        neighbors = []
        neighbors.append([y - 1, x])
        neighbors.append([y + 1, x])
        neighbors.append([y, x - 1])
        neighbors.append([y, x + 1])
        neighbors_valid = [neighbor for neighbor in neighbors
                        if neighbor[0] >= 0 #x가 0보다 같거나 커야 한다
                        and neighbor[0] < world_width # x가 world_width 보다 작아야 한다
                        and neighbor[1] >= 0 #y가 0보다 같거나 커야 한다
                        and neighbor[1] < world_height
                        and str(grid[neighbor[1]][neighbor[0]]) == target] #y가 world_width 보다 작아야 한다
        print("neighbors : ", neighbors_valid)
        return neighbors_valid

class Zebra(Animal):
    def __str__(self) -> str:
        return 'Z'
    
    def breed(self):
        if self.age >= 3:
            neighbors = self.get_neighbors(grid, ".")
            if len(neighbors) > 0:
                chosen_neighbor = random.choice(neighbors)
                x, y = chosen_neighbor
                new_zebra = Zebra(x, y)
                return new_zebra
        return None
        
    def move(self, grid):
        self.move_to(grid, target=".")

class Empty(Animal):
    def __str__(self) -> str:
        return '.'

class Lion(Animal):
    def __str__(self) -> str:
        return 'L'

    def breed(self):
        if self.age >= 8:
            neighbors = self.get_neighbors(grid, ".")
            if len(neighbors) > 0:
                chosen_neighbor = random.choice(neighbors)
                x, y = chosen_neighbor
                new_lion = Lion(x, y)
                return new_lion
        return None
    
    def move(self, grid):
        print(f'before: {self.x=}, {self.y=}')
        hunt_is_successful = self.move_to(grid, target="Z")
        if hunt_is_successful:
            self.hp = 3
        else:
            self.move_to(grid, target=".")
        print(f'after: {self.x=}, {self.y=}')
