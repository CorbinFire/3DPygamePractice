import pygame
import time
import sys
import math

pygame.init()
info = pygame.display.Info()
width = info.current_w
height = info.current_h
wn = pygame.display.set_mode((width-50,height-50))

class player:
    def __init__(self,id,username,x,y,z):
        self.id=id
        self.username=username
        self.x=x
        self.y=y
        self.z=z
        

class point:
    def __init__(self,x,y,z,connected_to):
        self.x = x
        self.y = y
        self.z = z
        self.connected_to = connected_to
    
    def draw_connected(self):
        pygame.draw.circle(wn,(0,255,0),[self.x,self.y],4)
        for i in self.connected_to:
            pygame.draw.line(wn,(255,0,0),[self.x,self.y],[i.x,i.y],width=2)

class square:
    def __init__(self,x,y,z,xs,ys,zs):
        self.thepoint=point(x+xs/2,y+ys/2,425,[])
        self.a=point(x,y,z,[])
        self.b=point(x+xs,y,z,[])
        self.c=point(x,y+ys,z,[])
        self.d=point(x+xs,y+ys,z,[])
        self.e=point(x,y,z-zs,[])
        self.f=point(x+xs,y,z-zs,[])
        self.g=point(x,y+ys,z-zs,[])
        self.h=point(x+xs,y+ys,z-zs,[])
        self.points=[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h]
        for i in self.points:
            for j in self.points:
                i.connected_to.append(j)

username=input("username: ")
id=input('id: ')
"player_"+username=player(id,username,width/2,height/2,0)
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
    
    if keys[pygame.K_UP]:
        count+=1
    else:
        count=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                place=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if place==True:
                place=False
                points.append(square(pygame.mouse.get_pos()[0]+a,pygame.mouse.get_pos()[1]+a,150,150,150,150))
                ##2
            
        
          
    if count > 1:
        ##1
        for i in points:
            for j in i.points:
                j.x-=((i.thepoint.x-j.x))/1000
                j.y-=((i.thepoint.y-j.y))/1000

    wn.fill((0,0,0))
    for i in points:
        for j in i.points:
            j.draw_connected()
    pygame.display.flip()
    lmp=pygame.mouse.get_pos()

##1
# dist = math.dist(lmp,pygame.mouse.get_pos())
# anglex = pygame.mouse.get_pos()[0]-lmp[0]
# angley = pygame.mouse.get_pos()[1]-lmp[1]
# print(anglex,'###',angley)

##2
# if  done == 2:
#     done+=1
#     # points.append(square(pygame.mouse.get_pos()[0]+b,pygame.mouse.get_pos()[1]+b,125,125))
# if  done == 3:
#     done+=1
#     # points.append(square(pygame.mouse.get_pos()[0]+c,pygame.mouse.get_pos()[1]+c,100,100))
# if  done == 4:
#     done+=1
#     points.append(square(pygame.mouse.get_pos()[0]+d,pygame.mouse.get_pos()[1]+d,75,75))
# if done == 5:
#     done+=1
#     # points.append(square(pygame.mouse.get_pos()[0]+e,pygame.mouse.get_pos()[1]+e,50,50))
# if done == 6:
#     done+=1
#     points.append(square(pygame.mouse.get_pos()[0]+f,pygame.mouse.get_pos()[1]+f,25,25))
# if done == 7:
#     done=1
#     points.append(square(pygame.mouse.get_pos()[0]+g,pygame.mouse.get_pos()[1]+g,5,5))
# # if done == 8:
# #     done+=1
# #     points.append(square(pygame.mouse.get_pos()[0]+g,pygame.mouse.get_pos()[1]+g,0,0))
# # if done == 9:
# #     done+=1
# #     points.append(square(pygame.mouse.get_pos()[0]+g,pygame.mouse.get_pos()[1]+g,0,0))
# # if done == 10:
# #     done+=1
# #     points.append(square(pygame.mouse.get_pos()[0]+g,pygame.mouse.get_pos()[1]+g,0,0))
