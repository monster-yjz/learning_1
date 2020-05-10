i = int(input('请输入一个数字：'))
list = []
[list.append(j) for j in range(1, i+1) if i % j == 0]
if len(list) == 2:
    print('是')
else:
    print('否')