import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# scatter(x,y)定义一个x，y坐标,及其他相关信息
plt.scatter(x_values, y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图标标题并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])
plt.show()

# plt.savefig('squares_plot.png')

