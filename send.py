import os
from time import sleep
a = ["/", "—", "|"]
al = ["/", "*",'-']
s = " "
t = 50
while True:
    for i in range (3):
        sleep(0.05)
        print(s * t, str(al[i]), end="\r")
        t = t - 1
        False
print("До самоуничтожения оталось: ")
n = 0
for i in range (60):
    sleep(1)
    print(60 - n, "Сек", end="\r")
    n += 1
for i in range (3):
    sleep(1)
    print(str(a[i]), end="\r")
print ('время кончилось')
sleep(2)
