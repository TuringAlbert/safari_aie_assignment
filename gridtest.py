grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(grid)):
    print(grid[i])

print(grid[1:2])

# def print_board(size=20):
#     # 상단 숫자 출력
#     print(' ', end='  ')
#     for i in range(size):
#         print(f'{i:2}', end=' ')
#     print()

#     # 바둑판 출력
#     for i in range(size):
#         print(f'{i:2}', end=' ')
#         for _ in range(size):
#             print('⬛ ', end='')
#         print()

# print_board()

# def create_board(size=19):
#     # Initialize a 19x19 grid with zeros
#     board = [[0]*size for _ in range(size)]
#     return board

# # Create a 19x19 Go board
# go_board = create_board()

# # Print the board
# for row in go_board:
#     print(row)

