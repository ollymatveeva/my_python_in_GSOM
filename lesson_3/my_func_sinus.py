from math import sin
def sinus(x):
    if 0.2<=x<=0.9:
        return sin(x)
    else: return 1

print(sinus(0.5))