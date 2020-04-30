from random import randint, choice
import matplotlib.pyplot as plt


class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认时为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1, self.num_sides)


die_1 = Die(6)
die_2 = Die(6)

i = 0
x = 0
y = 0
rw_x = []
rw_y = []
while True:
    for roll_num in range(0, 100):
        x_direction = choice([-1, 1])
        x_distance = x + die_1.roll()
        x_step = x_distance * x_direction

        y_direction = choice([-1, 1])
        y_distance = y + die_2.roll()
        y_step = y_distance * y_direction

        rw_x.append(x_step)
        rw_y.append(y_step)

    plt.scatter(rw_x, rw_y, c=rw_x, cmap=plt.cm.Blues(), edgecolors='none', s=15)
    i = i + 1
    if i > 100:
        break

plt.title("", fontsize=24)
plt.xlabel("Die 1", fontsize=14)
plt.ylabel("Die 2", fontsize=14)

plt.show()
