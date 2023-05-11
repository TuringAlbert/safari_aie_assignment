from animal_nk import Animal
import numpy as np
import matplotlib.pyplot as plt
import os


def print_TODO(todo):
    print(f'<<< NOT IMPLEMENTED : {todo} >>>')
    
class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.occupancy = [[False for _ in range(world_size)]]
        print_TODO('get random empty coordinates')
        self.zebras = [Animal(0,0) for _ in range(num_zebras)]
        self.lions = [Animal(0,0) for _ in range(num_lions)]
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')

    def display():
        print("Welcome to Safari!")
        print(" 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ")
        print("----------------------------------------------------")

    grid = [['O' for _ in range(20)] for _ in range(20)]

    print('   ', end=' ')
    for i in range(1, 21):
        print(f'{i:2}', end='')
    print()

    print('   ', end=' ')
    for i in range(1, 40):
        print(f'-', end='')
    print()


    for i in range(20):
        print(f'{i + 1:2}', '|', end=' ')
        for j in range(20):
            print(grid[i][j], end=' ')
        print()


        # os.system('cls') ##전부 사라지게 하는 코드
        
        # for i in range(20):
        #     print("--")
        # grid = np.zeros((20,20), dtype= int)
        # for i in range(20):
        #     row = (['0'] * 20)
        #     # row = row.append("\n")
        #     grid.append(row)
            
        #print(grid)
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
    
            
if __name__ == '__main__':
    safari = CircleOfLife(5,5,2)
    CircleOfLife.display()