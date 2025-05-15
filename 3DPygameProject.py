import pygame
import time
import math

pygame.init()
wn = pygame.display.set_mode((1400,900))

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
    def __init__(self,x,y,xs,ys):
        self.thepoint=point(x+xs/2,y+ys/2,425,[])
        self.a=point(x,y,500,[])
        self.b=point(x+xs,y,500,[])
        self.c=point(x,y+ys,500,[])
        self.d=point(x+xs,y+ys,500,[])
        self.e=point(x,y,350,[])
        self.f=point(x+xs,y,350,[])
        self.g=point(x,y+ys,350,[])
        self.h=point(x+xs,y+ys,350,[])
        self.points=[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h]
        for i in self.points:
            for j in self.points:
                i.connected_to.append(j)


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
    if pygame.mouse.get_pressed()[0]:
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
            if  done == 1 and place==True:
                place=False
                done+=1
                points.append(square(pygame.mouse.get_pos()[0]+a,pygame.mouse.get_pos()[1]+a,150,150))
            if  done == 2:
                done+=1
                # points.append(square(pygame.mouse.get_pos()[0]+b,pygame.mouse.get_pos()[1]+b,125,125))
            if  done == 3:
                done+=1
                # points.append(square(pygame.mouse.get_pos()[0]+c,pygame.mouse.get_pos()[1]+c,100,100))
            if  done == 4:
                done+=1
                points.append(square(pygame.mouse.get_pos()[0]+d,pygame.mouse.get_pos()[1]+d,75,75))
            if done == 5:
                done+=1
                # points.append(square(pygame.mouse.get_pos()[0]+e,pygame.mouse.get_pos()[1]+e,50,50))
            if done == 6:
                done+=1
                points.append(square(pygame.mouse.get_pos()[0]+f,pygame.mouse.get_pos()[1]+f,25,25))
            if done == 7:
                done=1
                points.append(square(pygame.mouse.get_pos()[0]+g,pygame.mouse.get_pos()[1]+g,5,5))
            # if done == 8:
            #     done+=1
            #     points.append(square(pygame.mouse.get_pos()[0]+g,pygame.mouse.get_pos()[1]+g,0,0))
            # if done == 9:
            #     done+=1
            #     points.append(square(pygame.mouse.get_pos()[0]+g,pygame.mouse.get_pos()[1]+g,0,0))
            # if done == 10:
            #     done+=1
            #     points.append(square(pygame.mouse.get_pos()[0]+g,pygame.mouse.get_pos()[1]+g,0,0))

        
          
        if count > 1:
            # dist = math.dist(lmp,pygame.mouse.get_pos())
            # anglex = pygame.mouse.get_pos()[0]-lmp[0]
            # angley = pygame.mouse.get_pos()[1]-lmp[1]
            # print(anglex,'###',angley)
            for i in points:
                for j in i.points:
                    j.x-=((i.thepoint.x-j.x))/1000
                    j.y-=((-i.thepoint.y-j.y))/1000

    wn.fill((0,0,0))
    for i in points:
        for j in i.points:
            j.draw_connected()
    pygame.display.flip()
    lmp=pygame.mouse.get_pos()