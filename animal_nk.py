
import random
from utils import print_TODO

class Animal:
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.age = 0
        self.hp = 3

    def move_to(self, grid, target) -> bool:
        ''' target can be ., L, or Z
            returns True if moved '''
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            grid[self.y][self.x] = Empty(self.y, self.x)
            chosen_neighbor = random.choice(neighbors)
            self.y, self.x = chosen_neighbor
            grid[self.y][self.x].hp = 0  # kill
            grid[self.y][self.x] = self
            return True
        else:
            return False

    def get_neighbors(self, grid, target):
        ''' target can be ., L, or Z
            returns a list of coordinates '''
        world_height = len(grid)
        world_width = len(grid[0])
        y, x = self.y, self.x
        neighbors = []
        neighbors.append([y - 1, x])
        neighbors.append([y + 1, x])
        neighbors.append([y, x - 1])
        neighbors.append([y, x + 1])
        neighbors_valid = [neighbor for neighbor in neighbors
                           if neighbor[0] >= 0
                           and neighbor[0] < world_height
                           and neighbor[1] >= 0
                           and neighbor[1] < world_width
                           and str(grid[neighbor[0]][neighbor[1]]) == target]
        return neighbors_valid

    def breed(self, grid):
        child = self.__class__(self.y, self.x)
        child.move_to(grid, target='.')
        grid[self.y][self.x] = self

class Empty(Animal):
    def __str__(self):
        return '.'

# class Zebra(Animal):
#     def __str__(self) -> str:
#         return 'Z'
    
    # def breed(self):
    #     if self.age >= 3:
    #         neighbors = self.get_neighbors(grid, ".")
    #         if len(neighbors) > 0:
    #             chosen_neighbor = random.choice(neighbors)
    #             x, y = chosen_neighbor
    #             new_zebra = Zebra(x, y)
    #             return new_zebra
    #     return None
        
    # def move(self, grid):
    #     self.move_to(grid, target=".")

    # def is_ready_to_breed(self):
    #     return self.age != 0 and self.age % 3 == 0

class Zebra(Animal):
    def __str__(self):
        return 'Z'

    def move(self, grid):
        self.move_to(grid, target='.')

    # def breed(self, grid):
    #     child_coords = self.get_neighbors(grid, '.')
    #     if len(child_coords) > 0:
    #         child_y, child_x = random.choice(child_coords)
    #         child = self.__class__(child_y, child_x)
    #         grid[child_y][child_x] = child

    def is_ready_to_breed(self):
        return self.age != 0 and self.age % 3 == 0


class Lion(Animal):
    def __str__(self):
        return 'L'

    # def breed(self):
    #     if self.age >= 8:
    #         neighbors = self.get_neighbors(grid, ".")
    #         if len(neighbors) > 0:
    #             chosen_neighbor = random.choice(neighbors)
    #             x, y = chosen_neighbor
    #             new_lion = Lion(x, y)
    #             return new_lion
    #     return None
    
    def move(self, grid):
        hunt_is_successful = self.move_to(grid, target='Z')
        if hunt_is_successful:
            self.hp = 3
        else:
            self.move_to(grid, target='.')
            self.hp -= 1

    def is_ready_to_breed(self):
        return self.age != 0 and self.age % 8 == 0