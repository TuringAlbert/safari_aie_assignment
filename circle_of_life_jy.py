
from animal_jy import Zebra, Lion, Animal
import numpy as np
import os


def print_TODO(todo):
    print(f'<<< NOT IMPLEMENTED : {todo} >>>')
class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.occupancy = [[False for _ in range(world_size)]
                          for _ in range(world_size)]
        print_TODO('get random empty coordinates')
        self.zebras = [Zebra(0,0) for _ in range(num_zebras)]
        self.lions = [Lion(0,0) for _ in range(num_lions)]
        self.timestep = 0
        self.grid = [[0 for _ in range(world_size)] 
                        for _ in range(world_size)]
        self.world_size = world_size + 1
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')

    def display(self):
        # #test of grid
        # print("test of grid : ")
        # print(self.grid)
        
        # 상단 숫자 및 Clock Timestep
        print('     ', end = '  ')
        for i in range(1, len(self.grid)+1):
            if i == len(self.grid):
                print(f'{i:2} time step = {self.timestep}')
            else:
                print(f'{i:2}', end=' ')
        
        # 상단 격자
        print('   ', end = '  ')
        top_coord_str = "-".join([ "-" for coord in range(31)])
        print(top_coord_str)
        for zebra in self.zebras:
            self.grid[zebra.y][zebra.x] = 'Z'
        for lion in self.lions:
            self.grid[lion.y][lion.x] = 'L'
      
        # 내부 값, 좌측 숫자 및 좌측/우측 격자 
        for i in range(0, len(self.grid)):
            print(f'{i:2}', end= '  ')
            print(f'{"|":2}', end= '  ')
            
            print(self.grid[i])
            #     for z in i:
            #         print(z, end='  ')
            # print(f'{"|":2}', end= '  ')
            # print() #enter
        
        # 하단 격자
        print('   ', end = '  ')
        top_coord_str = "-".join([ "-" for coord in range(31)])
        print(top_coord_str)
        
        # board = [[0]*self.world_size for _ in range(self.world_size)]
        
        # top_coord_str = " ".join([f'{coord}' for coord in range(self.world_size)]) #len(self.grid)
        # print(top_coord_str)
        
        key = input('enter [q] to quit:')
        os.system('clear') ##input 이후 전부 사라지게 하는 코드
        if key == 'q':
            exit()
        

    def step_move(self):
        print_TODO('step_move()')
        for lion in self.lions:
            direction = 'right'
            lion.move(direction)
            
        for zebra in self.zebras:
            print_TODO('get empty neighbor')
            direction = 'left'
            zebra.move(direction)
        
        # for lion in self.lions:
        #     print_TODO('get neighboring zebras')
        #     print_TODO('move to zebra if found, else move to empty')
        #     print_TODO('get empty neighbor')
        #     direction = 'right'
        #     lion.move(direction)
    
    def step_breed(self):
        print_TODO('step_breed()')
        # for animal in self.zebras + self.lions:
        #     print_TODO('get empty neighbor')
        #     x, y = 0, 0
        #     animal.breed(x, y)
            
    def run(self, num_timesteps=1000):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            
if __name__ == '__main__':
    safari = CircleOfLife(4,1,2) #worldsize, zebras, lions
    # safari.display()
    safari.run(100)
    # safari.step_move()
    # safari.step_breed()