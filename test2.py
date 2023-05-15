import random

import random

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = random.choice(directions)
        new_x, new_y = self.x + dx, self.y + dy
        # 초원 테두리 바깥으로는 동물이 나갈 수 없다.
        new_x = max(0, min(new_x, 19))
        new_y = max(0, min(new_y, 19))
        self.x, self.y = new_x, new_y

class Lion(Animal):
    pass

class Zebra(Animal):
    pass

class Plain:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.lions = []
        self.zebras = []

    def populate(self):
        # 시작시 사자 5마리/얼룩말 100마리
        for _ in range(5):
            while True:
                x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
                if self.grid[x][y] is None:
                    lion = Lion(x, y)
                    self.grid[x][y] = lion
                    self.lions.append(lion)
                    break
                
        for _ in range(100):
            while True:
                x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
                if self.grid[x][y] is None:
                    zebra = Zebra(x, y)
                    self.grid[x][y] = zebra
                    self.zebras.append(zebra)
                    break

    def timestep(self):
        for lion in self.lions:
            lion.move()
        for zebra in self.zebras:
            zebra.move()

plain = Plain(20)
plain.populate()

for _ in range(100):  # 100 timestep 진행
    plain.timestep()



