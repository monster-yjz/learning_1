import string

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

l = string.ascii_lowercase + "ab"  # 每次都是+2，所以后面多加了2个字母，这是小写字母表


def tran(s):
    tmp = ""
    for i in s:
        if i in l:  # 如果当前处理的字符是字母
            id = l.index(i)
            tmp += l[id + 2]
        else:
            tmp += i
    return tmp


print(tran(a))

# 输出了
"""i hope you didnt translate it by hand. thats what computers are for. " \
"doing it in by hand is inefficient and that's why this text is so long." \
" using string.maketrans() is recommended. now apply on the url. """

# 翻译过来就是：
# 我希望你不是徒手进行这个字符转换，这是计算机擅长的事情，徒手做是很低效的，所以我才把这个文本弄得这么长，将刚才你写的处理字符串的函数用在url上试试
