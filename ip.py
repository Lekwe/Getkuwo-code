import requests as r
import time

a2 = 0
a = 101
b = 43
c = 190
d = 152
while a2 == 0:
    req = r.get('http://'+str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
    d += 1
    print(req)
    time.sleep(1)
