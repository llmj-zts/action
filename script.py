import os
import urllib.request
os.mkdir("dist")
for i in range(5):
    f = urllib.request.urlopen("https://api.imlazy.ink/img")
    file = open("dist\\%d.png" % i, 'wb')
    file.write(f.read())
    file.close()
    print(i)
