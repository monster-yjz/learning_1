from random import randint
import matplotlib.pyplot as plt


class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认时为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1, self.num_sides)


die_1 = Die(15)
die_2 = Die(16)
x = []
y = []
i = 0

for roll_num in range(100):
    x.append(die_1.roll())
    y.append(die_2.roll())

while True:
    plt.scatter(x, y, c=x, cmap=plt.cm.Blues(), edgecolors='none', s=15)
    i = i + 1
    if i > 100:
        break

plt.title("", fontsize=24)
plt.xlabel("Die 1", fontsize=14)
plt.ylabel("Die 2", fontsize=14)

plt.show()
