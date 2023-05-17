from animal_nk import Animal
import numpy as np
#import matplotlib.pyplot as plt
import os
import random


def print_TODO(todo):
    print(f'<<< NOT IMPLEMENTED : {todo} >>>')
    
class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.occupancy = [[False for _ in range(world_size)]for _ in range(world_size)]
        print_TODO('get random empty coordinates')
        self.zebras = [Animal(0,0) for _ in range(num_zebras)]
        self.lions = [Animal(0,0) for _ in range(num_lions)]
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')

    def display(self):
        grid = [['O' for _ in range(20)] for _ in range(20)]

        def update_grid():
            num_L = 5
            num_Z = 100

            for _ in range(num_L):
                while True:
                    row = random.randint(0, 19)
                    col = random.randint(0, 19)
                    if grid[row][col] == 'O':
                        grid[row][col] = 'L'
                        break

            for _ in range(num_Z):
                while True:
                    row = random.randint(0, 19)
                    col = random.randint(0, 19)
                    if grid[row][col] == 'O':
                        grid[row][col] = 'Z'
                        break

        print('   ', end=' ')
        for i in range(1, 21):
            print(f'{i:2}', end='')
        print()

        print('   ', end=' ')
        for i in range(1, 41):
            print(f'-', end='')
        print()

        for i in range(20):
            print(f'{i + 1:2}', '|', end=' ')
            for j in range(20):
                print(grid[i][j], end=' ')
            print()

        # while True:
        #     user_input = input('enter or q')
        #     if user_input == '':
        #         update_grid()
        #         # time_step += 1
        #         # print(f'Time Step: {time_step}')
        #         print('   ', end=' ')
        #         for i in range(1, 21):
        #             print(f'{i:2}', end='')
        #         print()

        #         print('   ', end=' ')
        #         for i in range(1, 41):
        #             print(f'-', end='')
        #         print()

        #         for i in range(20):
        #             print(f'{i + 1:2}', '|', end=' ')
        #             for j in range(20):
        #                 print(grid[i][j], end=' ')
        #             print()
        #     elif user_input == 'q':
        #         break

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

if __name__ == '__main__':
    safari = CircleOfLife(5, 5, 2)
    safari.display()