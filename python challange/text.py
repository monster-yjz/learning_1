import zipfile

file = zipfile.ZipFile("channel.zip")

num = "90052"

content = file.read(num + '.txt')

print(content)
