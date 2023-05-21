import random
from utils import print_TODO


class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
    
    def move_to(self, grid, target) -> bool:
        '''target can be ., L, or Z
        returns True if moved
        '''
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor
            return True
        else:
            return False
    
    # def move(self, direction="right"):
    #     print(f'moving to {direction}. <<<NOT IMPLEMENTED YET>>>')
    #     self.x += 1
        
    def breed(self, x, y):
        print(f'breed for {x}, {y}. <<<NOT IMPLEMENTED YET>>>')
        # return Animal(x, y)
     
    def get_neighbors(self, grid, target):
        '''target can be '.', L, or Z
        returns a list of coordinates
        '''
        world_height = len(grid)
        world_width = len(grid[0])
        x, y = self.x, self.y
        neighbors = []
        neighbors.append([x - 1, y])
        neighbors.append([x + 1, y])
        neighbors.append([x, y - 1])
        neighbors.append([x, y + 1])
        print("neighbors : ", neighbors)
        neighbors_valid = [neighbor for neighbor in neighbors
                        if grid[neighbor[1]][neighbor[0]] == target
                        and neighbor[0] >= 0 #x가 0보다 같거나 커야 한다
                        and neighbor[0] < world_width # x가 world_width 보다 작아야 한다
                        and neighbor[1] >= 0 #y가 0보다 같거나 커야 한다
                        and neighbor[1] < world_height] #y가 world_width 보다 작아야 한다
        return neighbors_valid

class Zebra(Animal):
    # print(f'before : {self.x=}, {self.y=}')
    # def move(self, occupancy_grid):
    #     self.y += 1 
    #     print('<<< NOT IMPLEMENTED >>>')
    def breed(self, x, y):
        print('<<< NOT IMPLEMENTED >>>>>')
        
    def move(self, grid):
        # print(f'before: {self.x=}, {self.y=}')
        self.move_to(grid, target='.')
    
        # chosen_neighbor = random.choice(neighbors)
        # self.x, self.y = chosen_neighbor

            
        # print(f'after: {self.x=}, {self.y=}')
        
        # neighbors = self.get_neighbors(grid, target='.')
        # if len(neighbors) > 0:
        #     chosen_neighbor = random.choice(neighbors)
        # self.x, self.y = chosen_neighbor


class Lion(Animal):
    print_TODO('move to zebra if found')
    
    # def move(self,grid):
    #     self.x += 1
    #     print('<<< NOT IMPLEMENTED >>>')
    def move(self, grid):
        # print(f'before: {self.x=}, {self.y=}')
        hun_is_successful = self.move_to(grid, target='Z')
        if hun_is_successful:
            self.hp = 3
        else:
            self.move_to(grid, target='.')
        
        print(f'after: {self.x=}, {self.y=}')
        
        # neighbors = self.get_neighbors(grid, target='.')
        # if len(neighbors) > 0:
        #     chosen_neighbor = random.choice(neighbors)
        #     self.x, self.y = chosen_neighbor

