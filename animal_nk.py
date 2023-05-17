class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
        
    def move(self, direction):
        print(f'moving to {direction}. <<<NOT IMPLEMENTED YET>>>')
        
    def breed(self, x, y):
         return Animal(x, y)

    def get_neighbors(self, grid, target):
        world_height = len(grid)
        wirld_width = len(grid[0])

class Lion(Animal):
    def move(self, grid):
        print_TODO('get naighboring zebra')
        print_TODO('move to ')

class Zebra(Animal):
    def move(self, occupancy_grid):
        print('<<< NOT IMPLEMENTED >>>')
    def breed(self, x, y):
        print('<<< NOT IMPLEMENTED >>>>>')

class Zebra(Animal):
    def move(self, grid):
        print(f'before: {self.x=}, {self.y=}')
        neighbor = self.get_neighbors(grid, target='.')
        if len(neighbor) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor
        print(f'after: {self.x=}, {self.y=}')

class Lion(Animal):
    def move(self, grid):
        neighbors = self.get_neighbors(grid, target='Z')
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y =chosen_neighbor
            self.hp = 3
            return
        neighbors = self.get_neighbors(grid, target='.')

class get_neighbors(self, grid, target):
    world_height = len(grid)
    world_width = len(grid[0])
    x, y = self.x, self.y
    neighbor = []
    neighbor.append([x - 1, y])
    neighbor.append([x + 1, y])
    neighbor.append([x, y - 1])
    neighbor.append([x, y + 1])
    neighbor_valid = [neighbor for neighbor in get_neighborsif
                      if grid[neighbor[1]][neighbor[0]] == target
                      and neighbor[0] >= 0
                      and neighbor[0] < world_width
                      and neighbor[1] >= 0
                      and neighbor[1] < world_height]
    return neighbor_valid


