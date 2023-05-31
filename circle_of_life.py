from animal import Zebra, Lion, Empty
import numpy as np
import os
from utils import print_TODO
import random

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.grid = [[Empty(y,x) for y in range(self.world_size)]
                                 for x in range(self.world_size)] #len만큼의 grid 제작
        zebra_coords, lion_coords = self.get_random_coords(num_zebras, num_lions) #겹치지 않는 random coords 동물들의 위치를 입력
        random.seed(0)
        #동물 입력
        for y, x in zebra_coords:
            self.grid[y][x] = Zebra(y,x) #Zebra 매소드에서 'Z'를 출력
        for y, x in lion_coords:
            self.grid[y][x] = Lion(y,x) #Lion 매소드에서 'L'를 출력
        self.timestep = 0
        print('\nWelcome to AIE Safari!')
        print(f'\tWorld size = {world_size}')
        print(f'\tNumber of zebras = {num_zebras}')
        print(f'\tNumber of lions = {num_lions}\n')
        
    def get_random_coords(self, num_zebras, num_lions):
        all_coords = [(y, x) for y in range(self.world_size) for x in range(self.world_size)] #list 내 tuple 제작
       
        zebra_coords = random.sample(all_coords, num_zebras) #random.sample에서 num_zebras만큼 선택
        
        all_coords = list(set(all_coords) - set(zebra_coords)) #list 내 중복 tuple 삭제
        lion_coords = random.sample(all_coords, num_lions)#random.sample에서 num_lions만큼 선택
    
        return zebra_coords, lion_coords
    
    def display(self):
        # 상단 숫자 및 Clock Timestep
        # 상단 격자
        print('    ', end = ' ')
        for i in range(len(self.grid)):
            if i == len(self.grid)-1:
                print(f'{i+1}   / time step = {self.timestep}')
            elif i >= 8:
                print(f'{i+1} ', end='')
            else:
                print(f'{i+1} ', end=' ')
            
        print()
        print('   ', end = '')
        top_coord_str = "-".join([ " -" for coord in range(len(self.grid))])
        print(top_coord_str)
        #동물들을 grid 칸에 넣는다
        for row, line in enumerate(self.grid): #enumerate row에 index 삽입
            buffer = [str(animal) for animal in line]
            row = row
            print(f'{row+1:2} ' + f'{"| ":1}' +'  '.join(buffer) + f'{" |":1}')
        print('   ', end = '')
        top_coord_str = "-".join([ " -" for coord in range(len(self.grid))])
        print(top_coord_str)   
        
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
        
        key = input('press Enter to continue, press [q] to quit:')
        os.system('clear')
        if key == 'q':
            exit()
            
    def step_move(self):
        animals = [animal for line in self.grid for animal in line
                if not isinstance(animal, Empty)] #객체가 지정된 클래스나 튜플 안에 있는 클래스의 인스턴스인 경우 True 반환 isinstance(obj, class_or_tuple)
        
        # print("animals : ", animals)
        for animal in animals:
            if animal.hp != 0:
                animal.move(self.grid)     
                    
    def step_breed(self):
        animals = [animal for line in self.grid for animal in line
                if not isinstance(animal, Empty) #객체가 지정된 클래스나 튜플 안에 있는 클래스의 인스턴스인 경우 True 반환 isinstance(obj, class_or_tuple)
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
                     
    def update_grid(self):
        self.grid = [["." for _ in range(self.world_size)]
                          for _ in range(self.world_size)]
        for animal in self.zebras:
            self.grid[animal.y][animal.x] = "Z"
        for animal in self.lions:
            self.grid[animal.y][animal.x] = "L"
            
    def step_hunger(self):
        return
        for lion in self.lions:
            if lion.age >= 3:
                lion.hunger_count += 1
                if lion.hunger_count >= 3:
                    self.lions.remove(lion)  
          
    def clear_bodies(self):
        for y, line in enumerate(self.grid):
            for x, animal in enumerate(line):
                if animal.hp == 0:
                    self.grid[y][x] = Empty(y, x)
                    
    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            # self.display()
            self.step_breed()
            self.housekeeping()
            self.clear_bodies()
            self.display()
            
            
if __name__ == '__main__':
    # zebra = Zebra(0,0)
    # lion = Lion(0,0)
    # print(zebra.__class__)
    # print(Zebra)
    # print(lion.__class__)
    # print(Lion)
    # another_zebra = zebra.__class__(1,1)
    # another_lion = lion.__class__(1,1)
    # print(another_zebra)    
    # print(another_lion)

    safari = CircleOfLife(20,50,30) #worldsize, zebras, lions
    safari.run(300)
