import re
import zipfile

file = zipfile.ZipFile("channel.zip")

num = "90052"
comments = []
while True:
    # 打开文档.
    content = file.read(num + '.txt').decode("utf-8")
    comments.append(file.getinfo(num + '.txt').comment.decode("utf-8"))
    print(content)
    # 正则表达式确定字符位置，主要为数字
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))
