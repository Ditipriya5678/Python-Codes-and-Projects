import math

x= int(input())
y= int(input())
z= (pow(x,2)+pow(y,2))**(0.5)
p=z/2
q= (y/(2*p))
MBC= math.acos(q)
deg_MBC= math.degrees(MBC)
res=round(deg_MBC)
degree=chr(176)
print(res,degree,sep='')
