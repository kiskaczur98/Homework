import math
def kpt(x1,y1,x2,y2):
    e=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return e
a1=int(input("x1="))
b1=int(input("y1="))
a2=int(input("x2="))
b2=int(input("y2="))
print(kpt(a1,b1,a2,b2))