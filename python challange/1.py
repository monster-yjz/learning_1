s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. " \
    "rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
o = ''

for x in s:
    """遍历所有s中的字符"""
    """利用返回值判断是不是字母"""
    if ord('a') <= ord(x) <= ord('z'):

        # 嵌套一个ord（）+chr（）
        o += chr((ord(x) + 2 - ord('a')) % 26 + ord('a'))
    else:
        """a+= 1 等价于 a = a + 1"""
        # 非字母字符直接添加上去
        o += x
print(o)
