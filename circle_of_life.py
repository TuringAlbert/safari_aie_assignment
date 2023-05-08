from animal import Animal

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

    def display(self):
        print_TODO('display()')
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def step_move(self):
        print_TODO('step_move()')
        for zebra in self.zebras:
            print_TODO('get empty neighbor')
            direction = 'left'
            zebra.move(direction)
    
            
if __name__ == '__main__':
    safari = CircleOfLife(5,5,2)