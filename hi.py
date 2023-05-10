import matplotlib.pyplot as plt
import numpy as np

# 격자 크기 설정
grid_size = 20

# 격자 그리기
fig, ax = plt.subplots()
ax.set_xticks(np.arange(-0.5, grid_size, 1))
ax.set_yticks(np.arange(-0.5, grid_size, 1))
ax.grid(which='major', color='grey', linestyle='-', linewidth=1)
ax.imshow(np.zeros((grid_size, grid_size)))
plt.show()

##