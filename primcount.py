import math

i = 0
db = 0
while db<5:
    i = i +1
    szam = i
    prim = True
    j = 2
    gy = math.sqrt(szam)
    while prim and j <= szam:
        if szam % j == 0:
            prim = False
        else:
            j = j+1

    if prim:
        db = db+1