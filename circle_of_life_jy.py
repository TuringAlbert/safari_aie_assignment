from animal_jy import Animal
import numpy as np
import os


def print_TODO(todo):
    print(f'<<< NOT IMPLEMENTED : {todo} >>>')
    
class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.occupancy = [[False for _ in range(world_size)]
                          for _ in range(world_size)]
        print_TODO('get random empty coordinates')
        self.zebras = [Animal(0,0) for _ in range(num_zebras)]
        self.lions = [Animal(0,0) for _ in range(num_lions)]
        self.timestep = 0
        self.world_size = world_size + 1
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')

    def display(self):
        print("Welcome to Safari!")
        print(f'time step = {self.timestep}')
        # 상단 숫자 및 Clock Timestep
        print(' ', end = '  ')
        for i in range(1, self.world_size):
            if i == 20:
                print(f'{i:2} time step = {self.timestep}')
            else:
                print(f'{i:2}', end=' ')
        
        # 상단 격자
        print('   ', end = '  ')
        top_coord_str = "-".join([ "-" for coord in range(31)])
        print(top_coord_str)
            
        # 좌측 숫자 및 좌측/우측 격자 
        for i in range(1, self.world_size):
            print(f'{i:2}', end= '  ')
            print(f'{"|":2}', end= '  ')
            for _ in range(1, self.world_size):
                print('0', end='  ')
            print(f'{"|":2}', end= '  ')
            print() #enter
        
        # 하단 격자
        print('   ', end = '  ')
        top_coord_str = "-".join([ "-" for coord in range(31)])
        print(top_coord_str)
        
        # board = [[0]*self.world_size for _ in range(self.world_size)]
        
        # top_coord_str = " ".join([f'{coord}' for coord in range(self.world_size)]) #len(self.grid)
        # print(top_coord_str)
        
        
        # os.system('cls') ##input 이후 전부 사라지게 하는 코드
        
        # for i in range(20):
        #     print("--")
        grid = np.zeros((20,20), dtype= int)
        # print(grid)
        grid = [[0 for _ in range(20)] for _ in range(20)]
        for i in range(20):
            grid.append(i + 1)
        # print(grid)

            
    
        # print_TODO('display()')
        # key = input('enter [q] to quit:')
        # if key == 'q':
        #     exit()
            

    def step_move(self):
        print_TODO('step_move()')
        for zebra in self.zebras:
            print_TODO('get empty neighbor')
            direction = 'left'
            zebra.move(direction)
        for lion in self.lions:
            print_TODO('get neighboring zebras')
            print_TODO('move to zebra if found, else move to empty')
            print_TODO('get empty neighbor')
            direction = 'left'
            lion.move(direction)
    
    def step_breed(self):
        print_TODO('step_breed()')
        for animal in self.zebras + self.lions:
            print_TODO('get empty neighbor')
            x, y = 0, 0
            animal.breed(x, y)
            
if __name__ == '__main__':
    safari = CircleOfLife(20,100,5) #worldsize, zebras, lions
    safari.display()
    
    # safari.step_move()
    # safari.step_breed()