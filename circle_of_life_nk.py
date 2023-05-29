from animal_jy_nk import Zebra, Lion, Empty
# import numpy as np
import os
from utils import print_TODO
import random

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.grid = [[Empty(y, x) for y in range(self.world_size)]
                                  for x in range(self.world_size)]
        zebra_coords, lion_coords = self.get_random_coords(num_zebras, num_lions)
        for y, x in zebra_coords:
            self.grid[y][x] = Zebra(y, x) 
        for y, x in lion_coords:
            self.grid[y][x] = Lion(y, x)
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {num_zebras}')
        print(f'\tnumber of lions = {num_lions}')

    def get_random_coords(self, num_zebras, num_lions):
        all_coords = [(y, x) for y in range(self.world_size)
                       for x in range(self.world_size)]
        zebra_coords = random.sample(all_coords, num_zebras)
        all_coords = list(set(all_coords) - set(zebra_coords))
        lion_coords = random.sample(all_coords, num_lions)
        return zebra_coords, lion_coords

    # def display(self):
    #     print(f'Clock: {self.timestep}')
    #     for row in self.grid:
    #         buffer = [str(animal) for animal in row]
    #         print(' '.join(buffer))
    #     key = input('Enter [q] to quit:')
    #     if key == 'q':
    #         exit()

    def display(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(f'Clock: {self.timestep}')
        top_coord_str = ' '.join([f'{coord}' for coord in range(len(self.grid))])
        print('   ' + top_coord_str)
        for row, line in enumerate(self.grid):
            buffer = [str(animal) for animal in line]
            print(f'{row:2} ' + ' '.join(buffer))
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    # def display(self):
    #     self.update_grid()
    #     print('     ', end = '  ')
    #     for i in range(1, len(self.grid)+1):
    #         if i == len(self.grid):
    #             print(f'{i:2} time step = {self.timestep}')
    #         else:
    #                 print(f'{i:2}', end=' ')

    #     # 상단 격자
    #     print('   ', end = '  ')
    #     top_coord_str = "-".join([ "-" for coord in range(len(self.grid))])
    #     print(top_coord_str)
            
    #     for row, line in enumerate(self.grid):
    #         buffer = [str(animal) for animal in line]
    #         print(f'{row:2}' + ' '.join(buffer))
      
        # for zebra in self.zebras:
        #     self.grid[zebra.y][zebra.x] = 'Z'
        # for lion in self.lions:
        #     self.grid[lion.y][lion.x] = 'L'
        # print("self.grid : ", self.grid)
        # 내부 값, 좌측 숫자 및 좌측/우측 격자 
        # for i in range(0, len(self.grid)):
        #     print(f'{i:2}', end= '  ')
            # print(f'{"|":2}', end= '  ')
        # 하단 격자
        # print('   ', end = '  ')
        # top_coord_str = "-".join([ "-" for coord in range(31)])
        # print(top_coord_str)
        
        # key = input('enter [q] to quit:')
        # os.system('clear')
        # if key == 'q':
        #     exit()

    def step_move(self):
        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)]
        for animal in animals:
            if animal.hp != 0:
                animal.move(self.grid)

    def step_breed(self):
        # return
        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)
                   and animal.is_ready_to_breed()]
        for animal in animals:
            animal.breed(self.grid)

    def housekeeping(self):
        for y, line in enumerate(self.grid):
            for x, animal in enumerate(line):
                if animal.hp == 0:
                    self.grid[y][x] = Empty(y, x)
                else:
                    self.grid[y][x].age += 1

    # def step_hunger(self):
    #     # return
    #     lions = [lion for line in self.grid for lion in line
    #              if isinstance(lion, Lion)]
    #     for lion in lions:
    #         if lion.age >= 3:
    #             lion.hp -= 1
    #             if lion.hp == 0:
    #                 self.grid[lion.y][lion.x] = Empty(lion.y, lion.x)

    # def update_grid(self):
    #     self.grid = [["." for _ in range(self.world_size)]
    #                       for _ in range(self.world_size)]
    #     for animal in self.zebras:
    #         self.grid[animal.y][animal.x] = "Z"
    #     for animal in self.lions:
    #         self.grid[animal.y][animal.x] = "L"
            
    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()
            self.housekeeping()
            
if __name__ == '__main__':
    safari = CircleOfLife(5, 5, 2) #worldsize, zebras, lions
    safari.run(10)