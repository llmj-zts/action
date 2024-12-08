import os
import urllib.request
for i in range(5):
    f = urllib.request.urlopen("https://api.imlazy.ink/img")
    file = open("%d.png" % i, 'wb')
    file.write(f.read())
    file.close()
    print(i)
