#  C=(F - 32) \1.8
F = input('请输入需要转换的值')
if F.isalnum():
    C = (float(F) - 32)/1.8
    print('摄氏' + str(C) + '℃')
else:
    print('输入错误')


