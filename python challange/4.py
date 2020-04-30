"""http://www.pythonchallenge.com/pc/def/linkedlist.html"""

import requests

preurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
i = 12345
p = True
while p:
    url = preurl + str(i)
    text = requests.get(url).text
    i = text.split(" ")[-1]
    print(text)
    if i.isdigit:
        continue
    else:
        print(i)
        p = False


#运行了一会之后终于出了结果peak.html