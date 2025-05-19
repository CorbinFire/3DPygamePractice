import pygame
import time
import sys
import math
from classes_for_3D import *

pygame.init()
info = pygame.display.Info()
width = info.current_w
height = info.current_h
wn = pygame.display.set_mode((width-50,height-50))

        
# username=input("username: ")
# id=input('id: ')
player1=player('b','b',width/2,height/2,0)
print()
a=12.5
b=25
c=37.5
d=50
e=62.5
f=75
g=87.5
place=False
points=[]
done=1
count=0
lmp=pygame.mouse.get_pos()
running = True

while running:
    time.sleep(0.001)
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player1.z+=1
        for i in points:
            for j in i.points:
                j.x-=((i.centerpoint.x-j.x))/1000
                j.y-=((i.centerpoint.y-j.y))/1000
            # i.distancef()
    if keys[pygame.K_s]:
        player1.z-=1
        for i in points:
            for j in i.points:
                j.x+=((i.centerpoint.x-j.x))/1000
                j.y+=((i.centerpoint.y-j.y))/1000
            # i.distanceb()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                place=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if place==True:
                place=False
                points.append(square(pygame.mouse.get_pos()[0]+a,pygame.mouse.get_pos()[1]+a,150,150,150,150,wn,player1))
                ##2
            
        
          
    ##3 

    wn.fill((0,0,0))
    for i in points:
        for j in i.points:
            j.draw_connected()
    pygame.display.flip()
    lmp=pygame.mouse.get_pos()
