
from animal_jy import Zebra, Lion, Animal
import numpy as np
import os
from utils import print_TODO

# random choice neight
class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        # self.grid = [[False for _ in range(world_size)]
        #                   for _ in range(world_size)]
        # print_TODO('get random empty coordinates')
        self.zebras = [Zebra(0,0) for _ in range(num_zebras)]
        self.lions = [Lion(0,0) for _ in range(num_lions)]
        self.timestep = 0
        self.world_size = world_size
        self.reset_grid()

        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')
    def reset_grid(self):
        self.grid = [['.' for _ in range(self.world_size)] 
                        for _ in range(self.world_size)]
    def display(self):
            # 상단 숫자 및 Clock Timestep
            self.reset_grid() #grid를 다시 출력함으로서 초기화. grid에 동물을 출력하는 방법 (ANIMAL)
            print('     ', end = '  ')
            for i in range(1, len(self.grid)+1):
                if i == len(self.grid):
                    print(f'{i:2} time step = {self.timestep}')
                else:
                    print(f'{i:2}', end=' ')
            
            print("zebras : ", self.zebras)
            print("lions : ", self.lions)
            # 상단 격자
            print('   ', end = '  ')
            top_coord_str = "-".join([ "-" for coord in range(31)])
            print(top_coord_str)
            print("self.grid : ", self.grid)
            for zebra in self.zebras:
                self.grid[zebra.y][zebra.x] = 'Z'
            for lion in self.lions:
                self.grid[lion.y][lion.x] = 'L'
            print("self.grid : ", self.grid)
            # 내부 값, 좌측 숫자 및 좌측/우측 격자 
            for i in range(0, len(self.grid)):
                print(f'{i:2}', end= '  ')
                print(f'{"|":2}', end= '  ')
                print(self.grid[i]) # grid 출력하기
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
    
    def update_grid(self):
        self.grid = [['.' for _ in range(self.world_size)
                          for _ in range(self.world_size)]]
        for zebra in self.zebras:
            self.grid[zebra.y][zebra.x] = 'Z'
        for lion in self.lions:
            self.grid[lion.y][lion.x] = 'L'

    def step_move(self):
        # print_TODO('step_move()')
        for lion in self.lions:
            lion.move(self.grid)
            self.update_grid()
            
        for zebra in self.zebras:
            zebra.move(self.grid)
            self.update_grid
            # print("zebra : ",zebra)
            # print_TODO('get empty neighbor')
            # direction = 'left'
            # zebra.move(self.grid)
        
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
            
    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            # self.step_move()
            self.display()
            # self.step_breed()
            # self.display()
                
if __name__ == '__main__':
    safari = CircleOfLife(4,1,2) #worldsize, zebras, lions
    # safari.display()
    safari.run(100)
    # safari.step_move()
    # safari.step_breed()
    

