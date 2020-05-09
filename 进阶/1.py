# -*- coding:utf-8 -*-
from random import randint
from collections import deque


def main():
    i = randint(1, 10)
    hq = deque([], 5)
    times = 0
    P = True
    while P:
        j = input('请输入一个数字')
        if j.isdigit():
            n = int(j)
            hq.append(j)
            times += 1
            if int(n) > i:
                print("猜大了")
            elif int(n) < i:
                print("猜小了")
            elif int(n) == i:
                print("猜对了！")
                P = False
                print("一共猜了" + str(times) + '次')
            print('历史记录：' + '.'.join(hq))
        else:
            print('输入错误')


if __name__ == '__main__':
    main()
