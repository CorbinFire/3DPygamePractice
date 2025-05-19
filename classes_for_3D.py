import pygame
import math

def z_dis(point,points,centerpoint,player1):
    for i in points:
        z_distance=player1.z-point.z
        point.x+=(centerpoint.x-z_distance)/100
        point.y+=(centerpoint.y-z_distance)/100

class point:
    def __init__(self,x,y,z,connected_to,wn):
        self.x = x
        self.y = y
        self.z = z
        self.connected_to = connected_to
        self.wn = wn
    
    def draw_connected(self):
        pygame.draw.circle(self.wn,(0,255,0),[self.x,self.y],4)
        for i in self.connected_to:
            pygame.draw.line(self.wn,(255,0,0),[self.x,self.y],[i.x,i.y],width=2)


class square:
    def __init__(self,x,y,z,xs,ys,zs,wn,player):
        self.player=player
        self.centerpoint=point(x+xs/2,y+ys/2,z+zs/2,[],wn)
        self.a=point(x,y,z,[],wn)
        self.b=point(x+xs,y,z,[],wn)
        self.c=point(x,y+ys,z,[],wn)
        self.d=point(x+xs,y+ys,z,[],wn)
        self.e=point(x,y,z-zs,[],wn)
        self.f=point(x+xs,y,z-zs,[],wn)
        self.g=point(x,y+ys,z-zs,[],wn)
        self.h=point(x+xs,y+ys,z-zs,[],wn)
        self.a.connected_to.append(self.b)
        self.a.connected_to.append(self.c)
        self.a.connected_to.append(self.e)
        
        ######
        self.b.connected_to.append(self.a)
        self.b.connected_to.append(self.d)
        self.b.connected_to.append(self.f)
        
        ######
        self.c.connected_to.append(self.a)
        self.c.connected_to.append(self.d)
        self.c.connected_to.append(self.g)
        
        ######
        self.d.connected_to.append(self.b)
        self.d.connected_to.append(self.c)
        self.d.connected_to.append(self.h)
        
        ######
        self.e.connected_to.append(self.f)
        self.e.connected_to.append(self.g)
        self.e.connected_to.append(self.a)
        
        ######
        self.f.connected_to.append(self.h)
        self.f.connected_to.append(self.e)
        self.f.connected_to.append(self.b)
        
        ######
        self.g.connected_to.append(self.h)
        self.g.connected_to.append(self.e)
        self.g.connected_to.append(self.c)
        
        ######
        self.h.connected_to.append(self.g)
        self.h.connected_to.append(self.f)
        self.h.connected_to.append(self.d)
        
        ######
        self.points=[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h]
        z_dis(self.a,self.points,self.centerpoint,self.player)
        z_dis(self.b,self.points,self.centerpoint,self.player)
        z_dis(self.c,self.points,self.centerpoint,self.player)
        z_dis(self.d,self.points,self.centerpoint,self.player)
        z_dis(self.e,self.points,self.centerpoint,self.player)
        z_dis(self.f,self.points,self.centerpoint,self.player)
        z_dis(self.g,self.points,self.centerpoint,self.player)
        z_dis(self.h,self.points,self.centerpoint,self.player)


    def distancef(self):
        for i in self.points:
            z_distance=self.player.z-i.z
            i.x-=(self.centerpoint.x-z_distance)/1000
            i.y-=(self.centerpoint.y-z_distance)/1000

    def distanceb(self):
        for i in self.points:
            z_distance=self.player.z-i.z
            i.x+=(self.centerpoint.x-z_distance)/1000
            i.y+=(self.centerpoint.y-z_distance)/1000



class player:
    def __init__(self,id,username,x,y,z):
        self.id=id
        self.username=username
        self.x=x
        self.y=y
        self.z=z