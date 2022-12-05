import bpy
import random
from math import sqrt


L1=[] #hold list
L2=[] #main list
BallNumber=40

for i in range(3):
    x=random.randrange(0,16)
    L2.append(x)
    

while len(L2) < 3*BallNumber:
    for i in range(3):
        #coordinates
        x=random.randrange(0,16)
        L1.append(x)
    

    for i in range(0,len(L2),3):
        sayac = 1
       
        if(sqrt((L2[i]-L1[0])**2 + (L2[i+1]-L1[1])**2 + (L2[i+2]-L1[2])**2) <2):
            sayac=sayac-1
            break;

    if(sayac == 1):
        L2.append(L1[0])
        L2.append(L1[1])
        L2.append(L1[2])

    L1.clear()   
    print ('Liste2tekrar' , L2)
    
    #create
for i in range(0,len(L2),3):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(L2[i], L2[i+1], L2[i+2]), scale=(1, 1, 1))

    