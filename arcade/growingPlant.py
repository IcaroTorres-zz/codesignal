import math
def growingPlant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 1

    while height + upSpeed < desiredHeight:
        days += 1
        height += upSpeed - downSpeed
    return days

print growingPlant(100,10,910)
